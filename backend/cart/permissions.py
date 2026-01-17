from rest_framework import permissions

class IsCartItemOwner(permissions.BasePermission):
    # Custom permission to only allow owners of a cart item to access or modify it.
    def has_object_permission(self, request, view, obj):
        return obj.cart_id.user_id.id == request.user.id