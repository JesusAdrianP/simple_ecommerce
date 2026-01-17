from rest_framework import serializers
from .models import Order, OrderItem

class OrderSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Order
        fields = '__all__'
        extra_kwargs = {
            'id': {'read_only': True},
            'created_at': {'read_only':True}
        }
        
    def create(self, validated_data):
        order = Order.objects.create(**validated_data)
        order.save()
        return order
    
class OrderItemSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = OrderItem
        fields = '__all__'
        extra_kwargs = {
            'id': {'read_only':True}
        }
    
    def create(self, validated_data):
        orderItem = OrderItem.objects.create(**validated_data)
        orderItem.save()
        return orderItem