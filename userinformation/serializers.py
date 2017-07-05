from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Profile


class UserRegisterSerializer(serializers.ModelSerializer):
	tel_1 = serializers.Charfield(source='profile.tel_1')
	tel_2 = serializers.Charfield(source='profile.tel_2')
	address = serializers.Textfield(source='profile.address')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'password', 'email', 'tel_1', 'tel_2', 'address')