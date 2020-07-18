from django.contrib import admin
from product.models import *

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    model = Product
    # fields = [field.name for field in Product._meta.get_fields()[1:]]
    readonly_fields = ["user", "sales", "price", "avialable", "deleted"]
    list_display = [field.name for field in Product._meta.get_fields()]
    list_display_links = ("id", "name", "user")
    list_editable = ("price",)
    search_fields = ["name", "description", "user__username"]
    list_filter = ["category", "name"]
    list_per_page = 10


admin.site.register(Category)
