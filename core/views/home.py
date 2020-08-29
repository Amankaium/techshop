from django.shortcuts import redirect
from datetime import datetime


def home(request):
    # print(request.session)

    # value = datetime.now().strftime("%H:%M")
    # key = datetime.now().strftime("%d.%m.%Y %H:%M:%S")
    # request.session[key] = value

    # for key, value in request.session.items():
    #     print(key, value)        
    
    # del request.session["29.08.2020 19:38:03"]
    # del request.session["29.08.2020 19:38:06"]
    # del request.session["cart"]

    return redirect("products")