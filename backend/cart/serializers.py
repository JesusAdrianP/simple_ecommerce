from rest_framework import serializers
from .models import Cart, CartItem

class CartSerializer(serializers.ModelSerializer):
    
    class Meta:
        model= Cart
        fields = '__all__'
        extra_kwargs = {
            'id': {'read_only': True},
            'created_at': {'read_only':True},
            'updated_at': {'read_only':True}
        }
        
    def create(self, validated_data):
        cart = Cart.objects.create(**validated_data)
        cart.save()
        return cart
    
class CartItemSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = CartItem
        fields = '__all__'
        extra_kwargs = {
            'id': {'read_only': True},
            'added_at': {'read_only':True},
            'updated_at': {'read_only':True}
        }
    
    def create(self, validated_data):
        cartItem = CartItem.objects.create(**validated_data)
        cartItem.save()
        return cartItem

    
class CartItemUpdateSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = CartItem
        fields = '__all__'
        extra_kwargs = {
            'id': {'read_only': True},
            'cart_id' : {'read_only': True},
            'added_at': {'read_only': True},
            'updated_at': {'read_only': True},
            'product_id': {'read_only':True},
            'quantity': {'required':False}
        }
    
    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance