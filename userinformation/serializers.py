from rest_framework import serializers
from userinformation.models import Profile


class UserRegisterSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = ('id', 'email', 'password',
                  'first_name', 'last_name', 'tel_1',
                  'tel_2', 'address', 'city',
                  'country', 'zip_code')
        write_only_fields = ('password',)
        read_only_fields = ('id',)

    def create(self, validated_data):
        user = super(UserRegisterSerializer, self).create_user(validated_data)
        if 'password' in validated_data:
              user.set_password(validated_data['password'])
              user.save()
        return user
