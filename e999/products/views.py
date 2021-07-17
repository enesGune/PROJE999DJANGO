from django.shortcuts import render

# Create your views here.
from .models import Product


def product_view_detail(request):
    obj = Product.objects.get(id=1)
    context = {
        'title': obj.title,
        'description': obj.description,
        'price': obj.price,
        'summary': obj.summary,
    }
    return render(request, "product/detail.html", context)
