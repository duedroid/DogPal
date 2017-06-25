from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Profile


class UserViewSets(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name')

class ProfileSerializer(serializers.ModelSerializer):
    user = UserViewSets(many=True)
    class Meta:
        model = Profile
        fields = ('id', 'user', 'tel_1', 'tel_2', 'address', 'lineid', 'facebook')