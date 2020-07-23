from django.contrib.auth.decorators import user_passes_test
from django.contrib import auth
from django.shortcuts import render, redirect
from .user_not_authenticated import user_not_authenticated


@user_passes_test(user_not_authenticated)
def login(request):
    context = {}
    if "login" in request.POST:
        form = auth.forms.AuthenticationForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            auth.login(request, user)
            return redirect("home")

    context["form"] = auth.forms.AuthenticationForm()
    return render(request, "core/login.html", context)


def logout(request):
    auth.logout(request)
    return redirect("home")