from django.shortcuts import render,\
    HttpResponse, redirect


def test(request):
    return HttpResponse("test page")


def home(request):
    return redirect("products")