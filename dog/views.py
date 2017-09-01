from rest_framework import viewsets, mixins
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import detail_route, list_route
from account.permissions import IsUserAccount

from .serializers import *
from account.models import Account
from .models import *


class AddDogImageViewSet(mixins.CreateModelMixin,
                         viewsets.GenericViewSet):
    queryset = Picture.objects.all()
    serializer_class = DogImageUploadSerializer
    permission_classes = (IsUserAccount,)

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class AddorEditDogViewSet(mixins.CreateModelMixin,
                          mixins.UpdateModelMixin,
                          mixins.RetrieveModelMixin,
                          viewsets.GenericViewSet):
    queryset = Dog.objects.all()
    serializer_class = EditDogSerializer
    permission_classes = (IsUserAccount,)

    action_serializers = {
        'retrieve': EditDogSerializer,
        'create': AddDogSerializer,
        'update': EditDogSerializer,
        'partial_update': EditDogSerializer,
    }

    def get_serializer_class(self):
        if hasattr(self, 'action_serializers'):
            if self.action in self.action_serializers:
                return self.action_serializers[self.action]

        return super(AddorEditDogViewSet, self).get_serializer_class()

    def create(self, request):
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

    def update(self, request, pk=None, **kwargs):
        partial = kwargs.pop('partial', False)
        serializer = self.serializer_class(data=request.data, partial=partial)
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

    def partial_update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return self.update(request, *args, **kwargs)

    def retrieve(self, request, pk=None):
        dog = Dog.objects.filter(id=pk, account=request.user).first()
        serializer = EditDogSerializer(dog)
        return Response(serializer.data)


class DogViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Dog.objects.all()
    serializer_class = DogListSerializer
    permission_classes = (IsUserAccount,)

    def list(self, request):
        dog = Dog.objects.filter(account=request.user)
        serializer = self.get_serializer(dog, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        dog = Dog.objects.filter(id=pk).first()
        serializer = DogDetailSerializer(dog)
        return Response(serializer.data)

    @detail_route(methods=['get'])
    def delete(self, request, pk=None):
        dog = Dog.objects.filter(id=pk, account=request.user).first()
        if not dog:
            return Response({'Dog is not Exist'}, status=status.HTTP_400_BAD_REQUEST)
        dog.account = None
        dog.save(update_fields=['account'])

        return Response(status=status.HTTP_200_OK)

