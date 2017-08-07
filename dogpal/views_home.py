from rest_framework import viewsets, mixins
from .serializers import HomeSerializer
from userinformation.models import Profile
from doginformation.models import Dog
from rest_framework.response import Response


class HomeViewSet(mixins.ListModelMixin,
                  viewsets.GenericViewSet):
    queryset = Dog.objects.all()
    serializer_class = HomeSerializer

    def list(self, request):
        queryset = Dog.objects.all()
        serializer = HomeSerializer(queryset, many=True)
        return Response(serializer.data)
