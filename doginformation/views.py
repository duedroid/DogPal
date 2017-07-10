from rest_framework import viewsets, mixins
from doginformation.serializers import AddDogSerializer
from userinformation.models import Profile
from .models import Dog


class AddDogViewSet(mixins.CreateModelMixin,
                    viewsets.GenericViewSet):
    queryset = Dog.objects.all()
    serializer_class = AddDogSerializer
