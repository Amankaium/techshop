from django.shortcuts import render, redirect
from product.models import *
from product.forms import ProductForm


def products(request):
    context = {}
    context["products"] = Product.objects.filter(avialable=True)
    return render(request, "product/products.html", context)


def product(request, id):
    context = {}
    context["product"] = Product.objects.get(id=id)
    return render(request, "product/product.html", context)


def product_create(request):
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(products)
    
    context = {}
    context["form"] = ProductForm()

    return render(
        request,
        "product/form.html",
        context
    )
