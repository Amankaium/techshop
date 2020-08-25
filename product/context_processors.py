from product.models import Category
from feedback.forms import FeedBackForm


def category(request):
    context = {}
    context["categories"] = Category.objects.filter(parent_category=None).order_by("name")
    context["feedback_form"] = FeedBackForm()
    return context