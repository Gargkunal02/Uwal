from django.shortcuts import render

from shop.models import Contact, Product,Category

# Create your views here.

def index(request):
    product = None
    categories = Category.get_all_categories()
    categoryId = 11
    if categoryId:
        product = Product.get_all_products_by_id(categoryId)
    else:
        product = Product.get_all_products()
    data ={}
    data['product'] = product
    data['categories'] = categories
    return render(request,'portal/index.html',data)

def products(request):
    product = None
    categories = Category.get_all_categories()
    count1 = None
    categoryId = request.GET.get('category')
    product_type = request.GET.get('product')
    if categoryId:
        product = Product.get_all_products_by_id(categoryId)
        count1 = Product.get_all_products_by_id(categoryId).count()
    elif product_type:
        product = Product.get_all_products_by_product_id(product_type)
        count1 = Product.get_all_products_by_product_id(product_type).count()
    else:
        product = Product.get_all_products()
        count1 = Product.get_all_products().count()
    
    # sortPrice = Product.objects.order_by('Price')
    data ={}
    data['product'] = product
    data['categories'] = categories
    data['count'] = count1  
    # data['sortPrice'] = sortPrice
    return render(request,'portal/products.html',data)


def singleProduct(request,product_id):
    # product_id = request.GET.get('product_id')
    product = None
    obj = Product.objects.get(id=product_id)

    product={
        'object':obj,
    }
    
    print(product)
    return render(request,'portal/single-product-details.html',product)


# def AddProducts(request):
#     if request.method == 'GET':
#         return render(request,'portal/index.html')
#     else:
#         postData = request.POST
#         name = postData.get('name')
#         price = postData.get('price')
#         description = postData.get('Description')
#         product_type = postData.get('Product_type')
        
#         product = Product(name=name,price=price,Description=description,product_type=product_type)
        
#         product.save()
#         return render(request,'portal/index.html')
        
def contact(request):
    if request.method == 'POST':
        name=request.POST['name']
        email=request.POST['email']
        message=request.POST['message']
        contact = Contact(name=name, email=email, message=message)
        contact.save()
        return render(request,'portal/contact.html', {'m': 'Message sent successfully.'})
    return render(request,'portal/contact.html')
        