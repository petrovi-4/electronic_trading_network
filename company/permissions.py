from rest_framework.permissions import BasePermission


class IsActiveEmployee(BasePermission):

    def has_permission(self, request, view):
        if request.user and request.user.is_authenticated and request.user.is_active:
            return True
        return False
