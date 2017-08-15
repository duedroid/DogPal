from rest_framework import serializers
from account.models import Account


class UserRegisterSerializer(serializers.ModelSerializer):

    class Meta:
        model = Account
        fields = ('email', 'password', 'first_name',
                  'last_name', 'tel_1', 'tel_2',
                  'address', 'city', 'zip_code')
        write_only_fields = ('password')

class UserLogInSerializer(serializers.ModelSerializer):

    class Meta:
        model = Account
        fields = ('email', 'password')
