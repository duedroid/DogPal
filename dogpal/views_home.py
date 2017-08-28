from rest_framework import viewsets, mixins
from rest_framework import status
from rest_framework.response import Response
from account.permissions import IsUserAccount

from dog.models import Dog
from .serializers import HomeSerializer
from dog.serializers import DogListSerializer


class HomeViewSet(mixins.ListModelMixin,
                  viewsets.GenericViewSet):
    queryset = Dog.objects.all()
    serializer_class = HomeSerializer
    permission_classes = (IsUserAccount,)

    def list(self, request):
        dog = Dog.objects.filter(account=request.user)
        serializer = {
            'dog_list': DogListSerializer(dog, many=True).data,
            'appointment_list': HomeSerializer(dog, many=True).data
        }
        return Response(serializer)
