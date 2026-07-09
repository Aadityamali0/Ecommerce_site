from django.shortcuts import render
from django.http import HttpResponse
from . models import Product, Category

def home(request):
    products = Product.objects.all()
    category = Category.objects.all()
    params = {
        'product': products,
        'category' : category
    }
    print(category)
    return render(request, 'store/home.html', params)