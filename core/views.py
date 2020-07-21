from django.shortcuts import render,\
    HttpResponse, redirect
from django.contrib.auth.forms import AuthenticationForm, \
    UserCreationForm
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from core.forms import RegistrationForm
from product.models import Product


def test(request):
    return HttpResponse("test page")


def home(request):
    print("------------")
    print("Пользователь:")
    print(request.user)
    print("------------")
    return redirect("products")


def login(request):
    if request.user.is_authenticated:
        return redirect(home)
    context = {}
    if "login" in request.POST:
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            auth.login(request, user)
            return redirect(home)

    context["form"] = AuthenticationForm()
    return render(request, "core/login.html", context)


def logout(request):
    auth.logout(request)
    return redirect(home)


def registration(request):
    context = {}
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        password1 = request.POST["password1"]
        password2 = request.POST["password2"]
        if form.is_valid():
            form.save()
            return redirect("login")

    context["form"] = UserCreationForm()
    return render(request, "core/registration.html", context)


@login_required(login_url="/login/")
def profile(request, pk):
    context = {}
    context["user"] = User.objects.get(id=pk)
    context["products"] = Product.objects.filter(user=context["user"])
    return render(request, "core/profile.html", context)


def sellers(request):
    sellers = User.objects.exclude(product=None) 
    # User.objects.filter(product__in=products).distinct()
    context = {"sellers": sellers}
    return render(request, "core/sellers.html", context)