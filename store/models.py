from django.db import models

class Category(models.Model):
    category_name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.category_name
    
class Product(models.Model):
    product_name = models.CharField(max_length=50)
    price = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete = models.CASCADE, null = True, blank = True)
    description = models.CharField(max_length=300, default='')
    image = models.ImageField(upload_to = "store/product", default="")
    
    def __str__(self):
        return self.product_name
