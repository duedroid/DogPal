from django.contrib.auth import authenticate, login, logout
from rest_framework import viewsets, mixins
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from account.models import Account


class LogoutView(APIView):

    def post(self, request, format=None):
        if request.user.is_authenticated():
            logout(request)
            return Response(status=status.HTTP_200_OK)
        else:
            raise NotAuthenticated('Please login.')
