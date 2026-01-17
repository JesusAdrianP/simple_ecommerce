from rest_framework import permissions

class IsOrderOwner(permissions.BasePermission):
    # Custom permission to only allow owners of an order item to access or modify it.
    def has_object_permission(self, request, view, obj):
        return obj.user_id.id == request.user.id

class IsOrderItemOwner(permissions.BasePermission):
    # Custom permission to only allow owners of an order item to access or modify it.
    def has_object_permission(self, request, view, obj):
        return obj.order_id.user_id.id == request.user.id