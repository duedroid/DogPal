from rest_framework import viewsets, mixins
from rest_framework import status
from .serializers import HomeSerializer
from account.permissions import IsUserAccount

from dog.models import Dog
from rest_framework.response import Response


class HomeViewSet(mixins.ListModelMixin,
                  viewsets.GenericViewSet):
    queryset = Dog.objects.all()
    serializer_class = HomeSerializer
    permission_classes = (IsUserAccount,)

    def list(self, request):
        dog = Dog.objects.filter(account=request.user)
        serializer = {
            'appointment_list': HomeSerializer(dog, many=True).data
        }
        return Response(serializer)
