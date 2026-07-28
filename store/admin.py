from django.contrib import admin
from . models import Product, Category, SubImages


class SubImagesInlines(admin.TabularInline):
    model = SubImages
    extra = 4

class AdminProduct(admin.ModelAdmin):
    list_display = ['id', 'product_name', 'category', 'price']
    ordering = ['id']
    inlines = [SubImagesInlines]    

admin.site.register(Product, AdminProduct)
admin.site.register(Category)