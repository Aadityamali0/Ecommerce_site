from django.shortcuts import render
from django.http import HttpResponse
from .models import Product, Category

def home(request):
    categories = Category.objects.all()

    categoryID = request.GET.get('category')

    if categoryID:
        products = Product.objects.filter(category=categoryID)
    else:
        products = Product.objects.all()

    params = {
        'product': products,
        'category': categories
    }

    return render(request, 'store/home.html', params)

def signup(request):
    if request.method == 'GET':
        return render(request, 'store/signup.html')
    else:
        return HttpResponse('post invoked')
    # return render(request, 'store/signup.html')