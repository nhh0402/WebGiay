from django.contrib import admin
from django.urls import path
from webgiay_app import views

urlpatterns = [
    path('', views.index, name='index'),
    path('shop/', views.shop, name='shop'),
    path('product/<int:product_id>/', views.product_detail, name='product-detail'),
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('order-complete/', views.order_complete, name='order-complete'),
    path('contact/', views.contact, name='contact'),
    path('men/', views.men, name='men'),
    path('women/', views.women, name='women'),
    path('about/', views.women, name='about'),
    path('admin/', admin.site.urls),
]
