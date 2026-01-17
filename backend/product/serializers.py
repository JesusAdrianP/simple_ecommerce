from rest_framework import serializers
from .models import Category, Product

class CategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Category
        fields = '__all__'
        extra_kwargs = {
            'id': {'read_only':True}
        }
        
    def create(self, validated_data):
        category = Category.objects.create(**validated_data)
        category.save()
        return category

class ProductSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Product
        fields = '__all__'
        extra_kwargs = {
            'id': {'read_only': True},
            'created_at': {'read_only': True},
            'updated_at': {'read_only': True}
        }
    
    def create(self, validated_data):
        product = Product.objects.create(**validated_data)
        product.save()
        return product
    
class ProductUpdateSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Product
        fields = '__all__'
        extra_kwargs = {
            'id': {'read_only': True},
            'created_at': {'read_only': True},
            'updated_at': {'read_only': True},
            'name': {'required':False},
            'description': {'required':False},
            'price': {'required':False},
            'category_id': {'required':False},
            'image': {'required':False},
            'stock': {'required':False}
            
        }
    
    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance
    
class CategoryUpdateSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Category
        fields = '__all__'
        extra_kwargs = {
            'id': {'read_only':True},
            'name': {'required':False},
            'description': {'required':False}
        }
    
    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance