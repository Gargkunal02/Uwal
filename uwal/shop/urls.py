from django.urls import path
from shop.views import contact, index, products, singleProduct
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('',index,name='home'),
    path('products/',products,name='product'),
    path('products/<int:product_id>/',singleProduct,name='single_Product'),
    path('contact/',contact,name='contact'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

