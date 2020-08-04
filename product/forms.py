from django import forms
from product.models import *


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            "name",
            "category",
            "image",
            "description",
            "price",
        ]


# class CategoryCreateForm(forms.ModelForm):
#     class Meta:
#         model = Category
#         fields = ['name', 'description']

