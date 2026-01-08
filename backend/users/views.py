from django.shortcuts import render
from .serializers import CustomerUserSerializer
from rest_framework import generics, permissions

# Create your views here.

class CreateCustomUserView(generics.CreateAPIView):
    serializer_class = CustomerUserSerializer
    permission_classes = [permissions.AllowAny]