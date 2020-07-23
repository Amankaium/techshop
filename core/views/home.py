from django.shortcuts import redirect


def home(request):
    print("------------")
    # [print(f) for f in dir(request)]
    print(type(request))
    print("------------")
    return redirect("products")