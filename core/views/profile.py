from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm
from product.models import *


def profile(request, pk):
    context = {}
    context["user"] = User.objects.get(id=pk)
    context["products"] = Product.objects.filter(user=context["user"])
    context["password_change_form"] = PasswordChangeForm(request.user)
    context["category_count"] = Category.objects.filter(
        product__in=context["user"].product.all()
    ).distinct().count()

    return render(request, "core/profile.html", context)
