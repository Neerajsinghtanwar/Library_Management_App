from django.contrib.auth.models import Permission
from rest_framework.permissions import BasePermission

class MyPermission(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_superuser or request.user.user_permissions.filter(name='Can add user'):
            return True


class DefaultPermission(BasePermission):
    def has_permission(self, request, view):        
        user = request.user
        if user.is_authenticated:
            return True