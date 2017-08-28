from rest_framework import serializers
from account.models import Account


class UserRegisterSerializer(serializers.ModelSerializer):

    class Meta:
        model = Account
        fields = ('email', 'password', 'first_name',
                  'last_name', 'tel_1', 'tel_2',
                  'address', 'city', 'zip_code')
        write_only_fields = ('password')


class UserLogInSerializer(serializers.Serializer):

    email = serializers.CharField(max_length=255)
    password = serializers.CharField(min_length=4)


class UserAccountSerializer(serializers.ModelSerializer):

    class Meta:
        model = Account
        fields = ('id', 'email', 'first_name',
                  'last_name', 'tel_1', 'tel_2',
                  'address', 'city', 'zip_code')


class UserDogSerializer(serializers.ModelSerializer):
    account_id = serializers.SerializerMethodField()
    account_name = serializers.SerializerMethodField()
    dog = serializers.SerializerMethodField()

    class Meta:
        model = Account
        fields = ('account_id', 'account_name', 'dog')

    def get_dog(self, account):
        from dog.models import Dog
        from dog.serializers import DogNameListSerializer

        return DogNameListSerializer(Dog.objects.filter(account=account), many=True).data

    def get_account_name(self, account):
        return account.first_name + " " + account.last_name

    def get_account_id(self, account):
        return account.id
