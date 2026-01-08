from django.db import models

# Create your models here.

#category model
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True, blank=False, null=False)
    description = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return self.name

#product model
class Product(models.Model):
    name = models.CharField(max_length=200, blank=False, null=False)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=False, null=False)
    stock = models.IntegerField(blank=False, null=False)
    image = models.ImageField(upload_to='product_images/', blank=True, null=True)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)