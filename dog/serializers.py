from rest_framework import serializers

from account.models import Account
from .models import Dog, Picture
from veterinarian.models import Appointment, Hospital
from vaccination.models import VaccineRecord
from vaccination.serializers import VaccineRecordSerailizer
from utils.serializers import Base64ImageField


class DogImageUploadSerializer(serializers.Serializer):
    dog_id = serializers.IntegerField(required=True)
    image = Base64ImageField(max_length=None, use_url=False, allow_empty_file=True, allow_null=True, required=False)


class DogImageSerializer(serializers.ModelSerializer):
    image = Base64ImageField(max_length=None, use_url=False, allow_empty_file=True, allow_null=True, required=False)

    class Meta:
        model = Picture
        fields = ('id', 'image')


class AddorEditDogSerializer(serializers.ModelSerializer):

    class Meta:
        model = Dog
        fields = ('name', 'blood_type', 'breed', 'current_weight',
                  'age', 'birth_day', 'is_sterize', 'gender',
                  'micro_no', 'color_primary', 'color_secondary',
                  'location', 'dominance', 'status')


class DogListSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    class Meta:
        model = Dog
        fields = ('id', 'name', 'image')

    def get_image(self, dog):
        return DogImageSerializer(Picture.objects.filter(dog=dog).first()).data


class DogDetailSerializer(serializers.ModelSerializer):
    vaccine = serializers.SerializerMethodField()
    image = serializers.SerializerMethodField()

    class Meta:
        model = Dog
        fields = ('name', 'blood_type', 'breed', 'current_weight',
                  'age', 'birth_day', 'is_sterize', 'gender',
                  'micro_no', 'color_primary', 'color_secondary',
                  'location', 'dominance', 'vaccine', 'image')

    def get_vaccine(self, dog):
        vaccine = VaccineRecord.objects.filter(dog=dog, status=True)
        return VaccineRecordSerailizer(vaccine, many=True).data

    def get_image(self, dog):
        return DogImageSerializer(Picture.objects.filter(dog=dog), many=True).data


class DogNameListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Dog
        fields = ('name',)
