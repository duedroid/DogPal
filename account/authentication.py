from account.models import Account
from django.contrib.auth.hashers import check_password

from rest_framework.authentication import BasicAuthentication
from rest_framework import exceptions

class APIAuthentication(BasicAuthentication):
    def authenticate(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        if not email or not password:
            return None

        try:
            account = Account.objects.get(email=email)
            if not check_password(password, account.password):
                return None
        except Account.DoesNotExist:
            raise exceptions.AuthenticationFailed('No such account')

        return (account, None)
