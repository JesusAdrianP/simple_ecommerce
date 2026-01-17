from django.contrib.auth.hashers import check_password
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from .models import CustomUser

class CustomerUserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = CustomUser
        fields = ['id', 'email', 'first_name', 'last_name', 'password', 'role', 'phone_number']
        
        extra_kwargs = {
            'id':{'read_only':True},
            'password':{'write_only':True},
        }
        
    def create(self, validated_data):
        password = validated_data.pop('password')
        person = CustomUser(**validated_data)
        person.set_password(password)
        person.save()
        return person
    