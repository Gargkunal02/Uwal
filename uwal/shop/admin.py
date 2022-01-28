from django.contrib import admin

from shop.models import Category, Contact, Product

# Register your models here.

class AdminProduct(admin.ModelAdmin):
    list_display = ['name','price','Description','Category','product_type']

class AdminCategory(admin.ModelAdmin):
    list_display = ['name']
    
class Admincontact(admin.ModelAdmin):
    list_display = ['name','email','message']
    
    
admin.site.register(Product, AdminProduct)
admin.site.register(Category, AdminCategory)
admin.site.register(Contact, Admincontact)

