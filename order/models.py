from django.db import models
from product.models import Product


class Cart(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    phone = models.CharField(max_length=255, null=True, blank=True)


class ProductInCart(models.Model):
    cart = models.ForeignKey(
        to=Cart, on_delete=models.SET_NULL,
        null=True, blank=True,
        related_name="product_in_cart",
        verbose_name="Заказ")

    product = models.ForeignKey(
        to=Product, on_delete=models.SET_NULL,
        null=True, blank=True,
        related_name="product_in_cart",
        verbose_name="Товар")

    added = models.DateTimeField(
        auto_now_add=True,
        null=True,
        verbose_name="Время добавления"
    )