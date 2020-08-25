from django.shortcuts import render
from django.views.decorators.http import require_POST
from .forms import FeedBackForm

@require_POST
def feedback(request):
    context = {}
    form = FeedBackForm(request.POST, request.FILES)
    if form.is_valid():
        feedback = form.save()
        if request.user.is_authenticated:
            feedback.user = request.user
            feedback.save()

        context["message"] = "Ваше обращение принято, спасибо!"
        context["type"] = "success"
        return render(request, "core/message.html", context)

    context["message"] = "Форма заполнена неверно!"
    context["type"] = "warning"
    return render(request, "core/message.html", context)
