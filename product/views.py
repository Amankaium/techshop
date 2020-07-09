from django.shortcuts import render
from product.models import *


def products(request):
    context = {}
    context["products"] = Product.objects.filter(avialable=True)
    return render(request, "product/products.html", context)
