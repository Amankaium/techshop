from django.shortcuts import render, HttpResponse


def home(request):
    return HttpResponse("homepage")


def test(request):
    return HttpResponse("test page")
