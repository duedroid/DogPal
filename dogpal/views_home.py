from rest_framework import viewsets, mixins
from .serializers import HomeSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from dog.models import Dog
from rest_framework.response import Response


class HomeViewSet(mixins.ListModelMixin,
                  viewsets.GenericViewSet):
    queryset = Dog.objects.all()
    serializer_class = HomeSerializer
    permissions_classes = (IsAuthenticated,)

    def list(self, request):
        dog = Dog.objects.filter(account=request.user)
        serializer = HomeSerializer(dog, many=True)
        return Response(serializer.data)
