from rest_framework.permissions import BasePermission


class IsVeterinarianAccount(BasePermission):

    def has_permission(self, request, view):
        return (request.user.is_veterinarian and request.user.is_authenticated()) or request.user.is_admin


class IsUserAccount(BasePermission):

    def has_permission(self, request, view):
        return (not request.user.is_veterinarian and request.user.is_authenticated()) or request.user.is_admin
