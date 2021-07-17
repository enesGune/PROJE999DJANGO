from django.shortcuts import render

# Create your views here.
from .models import Product
from .forms import ProductForms, RawProductForm


# def product_create_view(request):
#     my_form = RawProductForm()
#     context = {
#         'form': my_form,
#     }
#     return render(request, "products/products_create.html", context)

# def product_create_view(request):
#     context = {}
#     if request.method == "POST":
#         my_new_title = request.POST.get('title')
#         # Product.objects.create(title=my_new_title)
#     return render(request, "products/products_create.html", context)

def product_create_view(request):
    initial_data = {
        'title': 'this'
    }

    form = ProductForms(request.POST or None, initial=initial_data)
    if form.is_valid():
        form.save()
    context = {
        'form': form,
    }
    return render(request, "products/products_create.html", context)


def product_view_detail(request):
    obj = Product.objects.get(id=1)
    # context = {
    #     'title': obj.title,
    #     'description': obj.description,
    #     'price': obj.price,
    #     'summary': obj.summary,
    # }
    context = {
        'obj': obj,
    }
    return render(request, "products/products_detail.html", context)
