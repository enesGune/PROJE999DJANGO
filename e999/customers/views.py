from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def home_view(request, *args, **kwargs):
    print(request.user)
    print(args, kwargs)
    return HttpResponse("<h1>Hello World</h1>")  # string html code


def about_view(request, *args, **kwargs):
    return HttpResponse("<h1>About Page</h1>")


def home_page(request, *args, **kwargs):
    return render(request, "home.html", {})
