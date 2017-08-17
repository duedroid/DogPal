from rest_framework import viewsets, mixins
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from dog.serializers import AddDogSerializer, DogDetailSerializer
from account.models import Account
from .models import Dog, Picture


class AddDogViewSet(mixins.CreateModelMixin,
                    viewsets.GenericViewSet):
    queryset = Dog.objects.all()
    serializer_class = AddDogSerializer
    permissions_classes = (IsAuthenticated,)

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
                dominance=serializer.data['dominance'])
            picture = Picture.objects.create(image=serializer.data['picture'], dog=dog)
            dog.save()
            picture.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)





class DogDetailViewSet(mixins.RetrieveModelMixin,
                       viewsets.GenericViewSet):
    queryset = Dog.objects.all()
    serializer_class = DogDetailSerializer
    permissions_classes = (IsAuthenticated,)

    def retrieve(self, request, pk=None):
        dog = Dog.objects.get(id=pk)
        serializer = DogDetailSerializer(dog)
        return Response(serializer.data)
