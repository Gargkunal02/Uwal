from django.contrib import admin

from shop.models import Category, Product

# Register your models here.

class AdminProduct(admin.ModelAdmin):
    list_display = ['name','price','Description','Category','product_type']

class AdminCategory(admin.ModelAdmin):
    list_display = ['name']
    
    
admin.site.register(Product, AdminProduct)
admin.site.register(Category, AdminCategory)