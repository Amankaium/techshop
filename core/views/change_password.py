from django.shortcuts import redirect
from django.views.decorators.http import require_http_methods
from django.contrib.auth.forms import PasswordChangeForm


@require_http_methods(["POST"])
def change_password(request):
    form = PasswordChangeForm(user=request.user, data=request.POST)
    if form.is_valid():
        form.save()
    
    return redirect("login")