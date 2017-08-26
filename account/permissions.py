from rest_framework.permissions import BasePermission


class IsVeterinarianAccount(BasePermission):

    def has_permission(self, request, view):
        if not request.user.is_authenticated():
            return False
        return request.user.is_veterinarian or request.user.is_admin


class IsUserAccount(BasePermission):

    def has_permission(self, request, view):
        if not request.user.is_authenticated():
            return False
        return not request.user.is_veterinarian or request.user.is_admin
