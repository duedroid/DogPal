from rest_framework import viewsets
from .serializers import UserRegisterSerializer
from django.contrib.auth.models import User


class UserRegisterViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer