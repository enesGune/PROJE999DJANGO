from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def home_view(request, *args, **kwargs):
    print(request.user)
    print(args, kwargs)
    return HttpResponse("<h1>Hello World</h1>")  # string html code


def about_view(request, *args, **kwargs):
    my_contex = {
        "my_title": "it is coll",
        "my_number": 12345,
        "my_list": [1234, 466, 5646, 44]
    }
    return render(request, "about.html", my_contex)


def home_page(request, *args, **kwargs):
    return render(request, "home.html", {})
