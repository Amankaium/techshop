from django.shortcuts import render
from .models import *

# Create your views here.
def cart(request):
    cart_id = request.session["cart"]
    cart = Cart.objects.get(id=cart_id)
    return render(request, "order/cart.html", {"cart": cart})