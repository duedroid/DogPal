from django.conf import settings
from rest_framework.compat import is_authenticated
from rest_framework.permissions import BasePermission
from rest_framework import permissions


class IsUserAccount(BasePermission):

    def has_permission(self, request, view):
        return request.user.is_veterinarian == False

    def has_object_permission(self, request, view, obj):
        return obj.id == request.user.id
