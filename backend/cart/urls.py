from django.urls import path
from .views import *

urlpatterns = [
    #cart urls
    path('cart-list', CartListView.as_view(), name='cart-list'),
    path('cart-create', CartCreateView.as_view(), name='cart-create'),
    
    #products urls
    path('cart-items-list', CartItemListView.as_view(), name='cart-items-list'),
    path('add-cart-product', CartItemCreateView.as_view(), name='add-cart-product'),
    path('update-cart-product/<int:pk>', CartItemUpdateView.as_view(), name='update-product-cart'),
    path('delete-cart-product/<int:pk>', CartItemDeleteView.as_view(), name='delete-product-cart'),
    
]