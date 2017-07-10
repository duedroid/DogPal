from rest_auth.registration.serializers import RegisterSerializer
from userinformation.models import Profile

# class RegistrationSerializer(RegisterSerializer):
#     first_name = serializers.CharField(required=True)
#     last_name = serializers.CharField(required=True)
#     tel_1

#     def get_cleaned_data(self):
#         return {
#             'first_name': self.validated_data.get('first_name', ''),
#             'last_name': self.validated_data.get('last_name', ''),
#             'username': self.validated_data.get('username', ''),
#             'password': self.validated_data.get('password', ''),
#             'email': self.validated_data.get('email', '')
#         }
