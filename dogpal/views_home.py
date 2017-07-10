from rest_framework import viewsets, mixins
from .serializers import HomeSerializer
from userinformation.models import Profile
from doginformation.models import Dog


class HomeViewSet(mixins.ListModelMixin,
                  viewsets.GenericViewSet):
    queryset = Profile.objects.all()
    serializer_class = HomeSerializer
