from django.contrib import admin
from . models import Product, Category, Customer

class AdminProduct(admin.ModelAdmin):
    list_display = ['id', 'product_name', 'category', 'price']
    ordering = ['id']
    
admin.site.register(Product, AdminProduct)
admin.site.register(Category)
admin.site.register(Customer)