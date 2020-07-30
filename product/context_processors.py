from product.models import Category


def category(request):
    context = {}
    context["categories"] = Category.objects.order_by("name")
    return context