from rest_framework import viewsets, mixins
from rest_framework.response import Response

from dog.serializers import AddDogSerializer, DogDetailSerializer
from account.models import Account
from .models import Dog


class AddDogViewSet(mixins.CreateModelMixin,
                    viewsets.GenericViewSet):
    queryset = Dog.objects.all()
    serializer_class = AddDogSerializer


class DogDetailViewSet(mixins.RetrieveModelMixin,
                       viewsets.GenericViewSet):
    queryset = Dog.objects.all()
    serializer_class = DogDetailSerializer

    def retrieve(self, request, pk=None):
        dog = Dog.objects.get(id=pk)
        serializer = DogDetailSerializer(dog)
        return Response(serializer.data)
