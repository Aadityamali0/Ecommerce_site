from django.shortcuts import render, get_object_or_404
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

# def signup(request):
#     if request.method == 'GET':
#         return render(request, 'store/signup.html')
#     else:
#         postData = request.POST
#         name = postData.get('name')
#         phone = postData.get('phone')
#         # print(name, email)
#         customer = Customer(name=name,
#                             phone=phone)
#         error_message = None
#         if not name:
#             error_message = "Name is required"
#         elif not phone:
#             error_message = "phone is required"
#         elif len(phone)<10:
#             error_message = "phone number must have 10 numbers"
        
#         if not error_message:
#             messages.success(request, 'signup successful')
#             customer.register()
#             return HttpResponse("Signup Successfull")
#         else:
#             return render(request, 'store/signup.html', {'error': error_message})

def product_details(request, slug, id):
    # product = Product.objects.get(id=id)
    product = get_object_or_404(Product, id=id)
    
    related_products = Product.objects.filter(
        category = product.category
    ).exclude(id=product.id).order_by('?')[:10]
    
    params = {
        'product' : product,
        'subimages': product.sub_images.all(),
        'relatedProducts' : related_products
    }
    
    return render(request, 'store/productDetailsPage.html', params)