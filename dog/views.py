from rest_framework import viewsets, mixins
from rest_framework import status
from rest_framework.response import Response
from rest_framework.parsers import JSONParser

from dog.serializers import *
from account.models import Account
from .models import Dog, Picture


class AddDogImageViewSet(mixins.CreateModelMixin,
                         viewsets.GenericViewSet):
    queryset = Picture.objects.all()
    serializer_class = DogImageUploadSerializer
    # parser_classes = (JSONParser,)

    def create(self, request):
        if request.user.is_veterinarian:
            return Response(status=status.HTTP_403_FORBIDDEN)

        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            dog = Dog.objects.filter(id=serializer.data['dog_id'], account=request.user).first()
            image = Picture.objects.create(image=serializer.data['image'], dog=dog)
            image.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AddorEditDogViewSet(mixins.CreateModelMixin,
                          mixins.UpdateModelMixin,
                          mixins.RetrieveModelMixin,
                          viewsets.GenericViewSet):
    queryset = Dog.objects.all()
    serializer_class = AddorEditDogSerializer

    def create(self, request):
        if request.user.is_veterinarian:
            return Response(status=status.HTTP_403_FORBIDDEN)

        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            dog = Dog.objects.create(
                account=request.user,
                name=serializer.data['name'],
                blood_type=serializer.data['blood_type'],
                breed=serializer.data['breed'],
                current_weight=serializer.data['current_weight'],
                age=serializer.data['age'],
                birth_day=serializer.data['birth_day'],
                is_sterize=serializer.data['is_sterize'],
                gender=serializer.data['gender'],
                micro_no=serializer.data['micro_no'],
                color_primary=serializer.data['color_primary'],
                color_secondary=serializer.data['color_secondary'],
                location=serializer.data['location'],
                dominance=serializer.data['dominance'],
                status=serializer.data['status'])
            dog.save()
            return Response({'id': dog.id}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        if request.user.is_veterinarian:
            return Response(status=status.HTTP_403_FORBIDDEN)

        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            dog = Dog.objects.filter(id=pk, account=request.user).first()
            dog.name = serializer.data['name']
            dog.blood_type = serializer.data['blood_type']
            dog.breed = serializer.data['breed']
            dog.current_weight = serializer.data['current_weight']
            dog.age = serializer.data['age']
            dog.birth_day = serializer.data['birth_day']
            dog.is_sterize = serializer.data['is_sterize']
            dog.gender = serializer.data['gender']
            dog.micro_no = serializer.data['micro_no']
            dog.color_primary = serializer.data['color_primary']
            dog.color_secondary = serializer.data['color_secondary']
            dog.location = serializer.data['location']
            dog.dominance = serializer.data['dominance']
            dog.status = serializer.data['status']
            dog.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        if request.user.is_veterinarian:
            return Response(status=status.HTTP_403_FORBIDDEN)

        dog = Dog.objects.filter(id=pk, account=request.user).first()
        serializer = AddorEditDogSerializer(dog)
        return Response(serializer.data)


class DogViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Dog.objects.all()
    serializer_class = DogListSerializer

    def list(self, request):
        if request.user.is_veterinarian:
            return Response(status=status.HTTP_403_FORBIDDEN)

        dog = Dog.objects.filter(account=request.user)
        serializer = self.get_serializer(dog, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        if request.user.is_veterinarian:
            return Response(status=status.HTTP_403_FORBIDDEN)

        dog = Dog.objects.filter(id=pk).first()
        serializer = DogDetailSerializer(dog)
        return Response(serializer.data)
