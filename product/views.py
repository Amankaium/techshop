from django.shortcuts import render, HttpResponse


def products(request):
    return HttpResponse("<h1>Список товаров:</h1>")
