from product.models import Category


def category(request):
    context = {}
    context["categories"] = Category.objects.filter(parent_category=None).order_by("name")
    return context