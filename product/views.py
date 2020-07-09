from django.shortcuts import render
from product.models import *


def products(request):
    context = {}
    context["products"] = Product.objects.filter(avialable=True)
    return render(request, "product/products.html", context)


def product(request, id):
    context = {}
    context["product"] = Product.objects.get(id=id)
    return render(request, "product/product.html", context)