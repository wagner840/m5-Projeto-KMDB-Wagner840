from rest_framework import permissions


class IsAdminOrReadOnly(permissions.BasePermission):
   
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
          
            return True
        else:
            return request.user.is_superuser


class IsCriticOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            return not request.user.is_superuser