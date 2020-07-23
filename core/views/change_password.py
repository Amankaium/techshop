from django.shortcuts import redirect
from django.views.decorators.http import require_http_methods


@require_http_methods(["POST"])
def change_password(request):
    user = request.user
    password_1 = request.POST.get("password_1")
    password_2 = request.POST.get("password_2")
    if password_1 == password_2:
        user.set_password(password_1)
        user.save()
    
    return redirect("profile", pk=user.id)