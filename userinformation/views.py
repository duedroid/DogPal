from rest_framework import viewsets, mixins
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from .serializers import UserRegisterSerializer
from userinformation.models import Profile


class UserRegisterViewSet(mixins.CreateModelMixin,
                          viewsets.GenericViewSet):
    queryset = Profile.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = UserRegisterSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
