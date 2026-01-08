from django.urls import path
from .views import *

urlpatterns = [
    #category urls
    path('categories-list', CategoryListView.as_view(), name='categories-list'),
    path('create-category', CategoryCreateView.as_view(), name='category-create'),
    path('category/<int:pk>', CategoryDetailView.as_view(), name='category-detail'),
    path('update-category/<int:pk>', CategoryUpdateView.as_view(), name='category-update'),
    path('delete-category/<int:pk>', CategoryDeleteView.as_view(), name='category-delete'),
    
    #products urls
    path('products-list', ProductListView.as_view(), name='products-list'),
    path('create-product', ProductCreateView.as_view(), name='product-create'),
    path('product/<int:pk>', ProductDetailView.as_view(), name='product-detail'),
    path('update-product/<int:pk>', ProductUpdateView.as_view(), name='product-update'),
    path('delete-product/<int:pk>', ProductDeleteView.as_view(), name='product-delete'),
    
]