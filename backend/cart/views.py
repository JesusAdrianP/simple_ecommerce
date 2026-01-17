from django.shortcuts import render
from .serializers import CartItemSerializer, CartSerializer, CartItemUpdateSerializer
from rest_framework import generics, permissions
from .models import Cart, CartItem
from .permissions import IsCartItemOwner

# Create your views here.

#views for creating carts and cart items
class CartCreateView(generics.CreateAPIView):
    serializer_class = CartSerializer
    permission_classes = [permissions.IsAuthenticated]
    
class CartItemCreateView(generics.CreateAPIView):
    serializer_class = CartItemSerializer
    permission_classes = [permissions.IsAuthenticated]
    
#Views for listing carts and cart items
class CartListView(generics.ListAPIView):
    serializer_class = CartSerializer
    permission_classes = [permissions.IsAdminUser]
    queryset = Cart.objects.all()
    
class CartItemListView(generics.ListAPIView):
    serializer_class = CartItemSerializer
    permission_classes = [permissions.IsAuthenticated, IsCartItemOwner]
    
    def get_queryset(self):
        my_user =  self.request.user
        queryset = CartItem.objects.filter(cart_id__user_id=my_user.id)
        return queryset
    
#views for updating cart items
class CartItemUpdateView(generics.UpdateAPIView):
    serializer_class = CartItemUpdateSerializer
    permission_classes = [permissions.IsAuthenticated, IsCartItemOwner]
    queryset = CartItem.objects.all()
    
#views for deleting cart items
class CartItemDeleteView(generics.DestroyAPIView):
    serializer_class = CartItemSerializer
    permission_classes = [permissions.IsAuthenticated, IsCartItemOwner]
    queryset = CartItem.objects.all()