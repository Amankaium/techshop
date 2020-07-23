from django.shortcuts import render
from django.contrib.auth.models import User


def sellers(request):
    sellers = User.objects.exclude(product=None) 
    # User.objects.filter(product__in=products).distinct()
    context = {"sellers": sellers}
    return render(request, "core/sellers.html", context)
