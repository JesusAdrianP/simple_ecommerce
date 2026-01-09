from django.shortcuts import render
from rest_framework import generics, permissions
from .serializers import OrderItemSerializer, OrderSerializer
from .models import Order, OrderItem
from .permissions import IsOrderItemOwner, IsOrderOwner

# Create your views here.

#views for creating orders and order items
class CreateOrderView(generics.CreateAPIView):
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]
    
class CreateOrderItemView(generics.CreateAPIView):
    serializer_class = OrderItemSerializer
    permission_classes = [permissions.IsAuthenticated]
    
#views for listing orders and order items
class ListOrderView(generics.ListAPIView):
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated, IsOrderOwner]
    def get_queryset(self):
        my_user =  self.request.user
        queryset= Order.objects.filter(user_id = my_user.id)
        return queryset
    
class ListOrderItemView(generics.ListAPIView):
    serializer_class = OrderItemSerializer
    permission_classes = [permissions.IsAuthenticated, IsOrderItemOwner]
    
    def get_queryset(self):
        my_user = self.request.user
        return OrderItem.objects.filter(order_id__user_id = my_user.id)