from django.contrib.auth import authenticate, login, logout
from rest_framework import viewsets, mixins
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed, PermissionDenied, NotAuthenticated
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from .authentication import APIAuthentication
from rest_framework.views import APIView

from .serializers import UserLogInSerializer
from account.models import Account


class UserLoginViewSet(mixins.CreateModelMixin,
                       viewsets.GenericViewSet):
    queryset = Account.objects.all()
    authentication_classes = (APIAuthentication,)
    permissions_classes = (AllowAny,)
    allow_redirects = True
    serializer_class = UserLogInSerializer

    def create(self, request, *args, **kwargs):
        import re
        if request.user.is_authenticated():
            raise PermissionDenied('Please logout.')

        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            email = serializer.data.get('email') or request.user
            password = serializer.data.get('password')
            msg = None

            email_regex = re.compile(r'[^@]+@[^@]+\.[^@]+')
            if email_regex.match(email):
                msg = 'This email or password is not valid.'

            user = authenticate(email=email, password=password)
            if not user:
                raise AuthenticationFailed(msg)
            login(request, user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LogoutView(APIView):

    def post(self, request, format=None):
        if request.user.is_authenticated():
            logout(request)
            return Response(status=status.HTTP_200_OK)
        else:
            raise NotAuthenticated('Please login.')
