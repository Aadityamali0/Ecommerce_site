from django.shortcuts import render
from django.http import HttpResponse
from . models import Product

def home(request):
    products = Product.objects.all()
    params = {
        'product': products
    }
    return render(request, 'store/home.html', params)