from django.urls import path
from .views import *

urlpatterns = [
    #oder urls
    path('create-order', CreateOrderView.as_view(), name='create-order'),
    path('list-orders', ListOrderView.as_view(), name='list-orders'),
    #orderitem urls
    path('create-order-item', CreateOrderItemView.as_view(), name='create-order-item'),
    path('list-order-items', ListOrderItemView.as_view(), name='list-order-items')
]