from rest_framework import viewsets, mixins
from rest_framework import status
from .serializers import HomeSerializer
from rest_framework.permissions import IsAuthenticated

from dog.models import Dog
from rest_framework.response import Response


class HomeViewSet(mixins.ListModelMixin,
                  viewsets.GenericViewSet):
    queryset = Dog.objects.all()
    serializer_class = HomeSerializer
    permissions_classes = (IsAuthenticated,)

    def list(self, request):
        if request.user.is_veterinarian:
            return Response(status=status.HTTP_403_FORBIDDEN)
        dog = Dog.objects.filter(account=request.user)
        serializer = HomeSerializer(dog, many=True)
        return Response(serializer.data)
