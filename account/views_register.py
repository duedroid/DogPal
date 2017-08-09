from rest_framework import viewsets, mixins
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from .serializers import UserRegisterSerializer
from account.models import Account


class UserRegisterViewSet(mixins.CreateModelMixin,
                          viewsets.GenericViewSet):
    queryset = Account.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = UserRegisterSerializer

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            user = Account.objects.create_user(
                email = serializer.data['email'],
                first_name = serializer.data['first_name'],
                last_name = serializer.data['last_name'],
                tel_1 = serializer.data['tel_1'],
                address = serializer.data['address'],
                city = serializer.data['city'],
                zip_code = serializer.data['zip_code'],
            )
            if serializer.data['tel_2']:
                user.tel_2 = serializer.data['tel_2']
            user.set_password(serializer.data['password'])
            user.save()
            return Response(UserRegisterSerializer(instance=user).data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
