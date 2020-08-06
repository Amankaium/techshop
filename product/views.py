from django.shortcuts import render, redirect
from django.db.models import Q
from django.contrib.auth.decorators import login_required, \
    user_passes_test
from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms import formset_factory
from django.forms.models import modelformset_factory
from django.urls import reverse, reverse_lazy
from django.views.generic import TemplateView, DetailView, \
    CreateView, View, ListView
from django.utils.decorators import method_decorator
from product.models import *
from product.forms import *
from product.mixins import IsStaffAccessMixin


def products(request):
    context = {}
    if "query" in request.GET:
        word = request.GET.get("query")
        context["object_list"] = Product.objects.filter(
            Q(avialable=True),
            Q(deleted=False),
            Q(name__contains=word) |
            Q(description__contains=word) |
            Q(category__name__contains=word)   
        )
    else:
        context["object_list"] = Product.objects.filter(
            avialable=True,
            deleted=False
        )
    return render(request, "product/products.html", context)


class ProductList(ListView):
    model = Product
    template_name = "product/products.html"
    queryset = Product.objects.filter(
        avialable=True,
        deleted=False
    )    


def product(request, id):
    context = {}
    context["product"] = Product.objects.get(id=id)
    return render(request, "product/product.html", context)


class ProductView(TemplateView):
    template_name = "product/product.html"

    def get_context_data(self, **kwargs):
        context = {}
        pk = self.kwargs["pk"]
        product = Product.objects.get(id=pk)
        context["product"] = product
        return context


class ProductDetailView(DetailView):
    template_name = "product/product.html"
    model = Product



@login_required(login_url="login")
def product_create(request):
    context = {}
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            new_product = form.save()
            new_product.user = request.user
            new_product.save()
            context["products"] = Product.objects.filter(
                avialable=True,
                deleted=False                
            )
            context["message"] = "Товар был успешно добавлен"
            return render(request, "product/products.html", context)
    
    context["form"] = ProductForm()

    return render(
        request,
        "product/create.html",
        context
    )


class ProductCreate(View):
    def get(self, *args, **kwargs):
        context = {}
        context["form"] = ProductForm()

        return render(
            self.request,
            "product/create.html",
            context
        )

    def post(self, *args, **kwargs):
        context = {}

        form = ProductForm(self.request.POST, self.request.FILES)
        if form.is_valid():
            new_product = form.save()
            new_product.user = self.request.user
            new_product.save()
            context["products"] = Product.objects.filter(
                avialable=True,
                deleted=False                
            )
            context["message"] = "Товар был успешно добавлен"
        return render(self.request, "product/products.html", context)


class ProductCreateView(LoginRequiredMixin, CreateView):
    login_url = "/login/"
    model = Product
    fields = [
                "name",
                "category",
                "image",
                "description",
                "price",
            ]
    # form = ProductForm
    template_name = "product/create.html"
    success_url = reverse_lazy("products")


@login_required(login_url="login")
def product_edit(request, id):
    product = Product.objects.get(id=id)
    if request.user != product.user:
        return redirect("home")

    context = {}

    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            context["product"] = Product.objects.get(id=id)
            context["message"] = "Информация успешно обновлена"
            return render(request, "product/product.html", context)
    
    context["form"] = ProductForm(instance=product)

    return render(
        request,
        "product/form.html",
        context
    )

@login_required(login_url='/login/')
def product_delete(request, id):
    product = Product.objects.get(id=id)
    context = {}

    if product.user != request.user:
        context["message"] = "У вас нет доступа!"
    else:
        product.deleted = True
        product.save()
        context["message"] = "Товар был удалён"
    
    context["type"] = "danger"
    return render(request, "core/message.html", context)


def category(request, pk):
    context = {}
    category = Category.objects.get(id=pk)
    context["object_list"] = Product.objects.filter(
        Q(category=category) |
        Q(category__in=category.child_category.all()),
        avialable=True,
        deleted=False
    )
    context["category_pk"] = pk
    return render(request, "product/products.html", context)


def create_few(request):
    ProductFormSet = modelformset_factory(
        model=Product,
        form=ProductForm,
        extra=2
    )
    context = {}

    if request.method == "POST":
        formset = ProductFormSet(request.POST, request.FILES)
        if formset.is_valid():
            formset.save()
            return redirect(reverse("home"))

    context["formset"] = ProductFormSet(queryset=Product.objects.none())

    return render(request, "product/create_few.html", context)

# @user_passes_test(lambda user: user.is_staff)
# def category_create(request):
#     context = {}

#     if request.method == "POST":
#         form = CategoryCreateForm(request.POST)
#         if form.is_valid():
#             category = form.save()
#             return redirect("category", pk=category.id)

#     context["form"] = CategoryCreateForm()
#     return render(request, "product/create_category.html", context)


class CategeryCreate(IsStaffAccessMixin, CreateView):
    model = Category
    fields = ["name", "description"]
    template_name = "product/create_category.html"
    success_url = reverse_lazy("products")

    # @method_decorator(user_passes_test(lambda user: user.is_staff))
    # def dispatch(self, *args, **kwargs):
    #     return super().dispatch(*args, **kwargs)