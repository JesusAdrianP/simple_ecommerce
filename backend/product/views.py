from django.shortcuts import render
from .serializers import ProductSerializer, CategorySerializer, CategoryUpdateSerializer, ProductUpdateSerializer
from rest_framework import generics, permissions
from .models import Category, Product

# Create your views here.

#Views for creating categories and products
class CategoryCreateView(generics.CreateAPIView):
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAdminUser]

class ProductCreateView(generics.CreateAPIView):
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAdminUser]
    
#views for listing categories and products
class CategoryListView(generics.ListAPIView):
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = Category.objects.all()
    
class ProductListView(generics.ListAPIView):
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = Product.objects.all()
    
#views for retrieving products and categories
class ProductDetailView(generics.RetrieveAPIView):
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = Product.objects.all()
    
class CategoryDetailView(generics.RetrieveAPIView):
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = Category.objects.all()

#views for updating products and categories
class ProductUpdateView(generics.UpdateAPIView):
    serializer_class = ProductUpdateSerializer
    permission_classes = [permissions.IsAdminUser]
    queryset = Product.objects.all()
    
class CategoryUpdateView(generics.UpdateAPIView):
    serializer_class = CategoryUpdateSerializer
    permission_classes = [permissions.IsAdminUser]
    queryset = Category.objects.all()

#views for deleting products and categories
class ProductDeleteView(generics.DestroyAPIView):
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAdminUser]
    queryset = Product.objects.all()
    
class CategoryDeleteView(generics.DestroyAPIView):
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAdminUser]
    queryset = Category.objects.all()