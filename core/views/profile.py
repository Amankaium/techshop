from django.shortcuts import render
from django.contrib.auth.models import User
from core.forms import ChangePasswordForm
from product.models import Product


def profile(request, pk):
    context = {}
    context["user"] = User.objects.get(id=pk)
    context["products"] = Product.objects.filter(user=context["user"])
    context["password_change_form"] = ChangePasswordForm()
    return render(request, "core/profile.html", context)
