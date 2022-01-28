# from typing_extensions import Required
import email
from email import message
from unicodedata import name
from django.db import models
from django.forms import CharField
# from django.db.models.fields import BLANK_CHOICE_DASH

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=90)
    
    def __str__(self):
        return self.name
    
    @staticmethod
    def get_all_categories():
        return Category.objects.all()

class Product(models.Model):
    name = models.CharField(max_length=60)
    price = models.IntegerField(default=0)
    Description = models.CharField(max_length=450,default='')
    Category = models.ForeignKey(Category ,on_delete=models.CASCADE, default='Uwal')
    image = models.ImageField(upload_to = 'upload/products/',default='upload/products/no-preview.png')
    image2 = models.ImageField(upload_to = 'upload/products2/',default='upload/products/no-preview.png')
    image3 = models.ImageField(upload_to = 'upload/products3/',default='upload/products/no-preview.png')
    product_type = models.CharField(max_length=60)

    
    @staticmethod
    def get_all_products():
        return Product.objects.all()
    
    @staticmethod
    def get_all_products_by_id(category_id):
        if category_id:
            return Product.objects.filter(Category=category_id)
        else:
            return Product.objects.all()
        
    @staticmethod
    def get_all_products_by_product_id(product_type):
        if product_type:
            return Product.objects.filter(product_type=product_type)
        else:
            return Product.objects.all()
        

class Contact(models.Model):
    name = models.CharField(max_length=330)
    email = models.EmailField(max_length=254)
    message = models.CharField(max_length=5000)
    