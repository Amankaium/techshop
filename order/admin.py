from django.contrib import admin
from .models import *

class ProductInCartInline(admin.StackedInline):
    model = ProductInCart
    extra = 0


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    model = Cart
    list_display = ["name", "phone", "get_product_count"]
    inlines = [
        ProductInCartInline
    ]

    def get_product_count(self, obj):
        return obj.product_in_cart.count()


@admin.register(ProductInCart)
class ProductInCartAdmin(admin.ModelAdmin):
    model = ProductInCart
    list_display = ("cart", "product", "added")
    readonly_fields = ("cart", "product", "added")
