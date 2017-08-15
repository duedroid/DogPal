from rest_framework import viewsets, mixins
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from dog.serializers import AddDogSerializer, DogDetailSerializer
from account.models import Account
from .models import Dog


class AddDogViewSet(mixins.CreateModelMixin,
                    viewsets.GenericViewSet):
    queryset = Dog.objects.all()
    serializer_class = AddDogSerializer
    permissions_classes = (IsAuthenticated,)
    authentication_classes = (JSONWebTokenAuthentication,)

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            dog = Dog.objects.create(serializer.data)
            dog.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DogDetailViewSet(mixins.RetrieveModelMixin,
                       viewsets.GenericViewSet):
    queryset = Dog.objects.all()
    serializer_class = DogDetailSerializer
    permissions_classes = (IsAuthenticated,)
    authentication_classes = (JSONWebTokenAuthentication,)

    def retrieve(self, request, pk=None):
        dog = Dog.objects.get(id=pk)
        serializer = DogDetailSerializer(dog)
        return Response(serializer.data)
