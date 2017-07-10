from rest_framework import viewsets
from doginformation.serializers import HomeSerializer
from userinformation.models import Profile


class HomeViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = HomeSerializer
