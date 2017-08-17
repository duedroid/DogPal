from rest_framework import serializers

from account.models import Account
from .models import Dog, Picture
from veterinarian.models import Appointment, Hospital
from vaccination.models import VaccineRecord
from vaccination.serializers import VaccineRecordSerailizer


class DogPictureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Picture
        fields = ('id', 'image')


class AddDogSerializer(serializers.ModelSerializer):

    class Meta:
        model = Dog
        fields = ('name', 'blood_type', 'breed', 'current_weight',
                  'age', 'birth_day', 'is_sterize', 'gender',
                  'micro_no', 'color_primary', 'color_secondary',
                  'location', 'dominance')

    def to_representation(self, instance):
        data = super(AddDogSerializer, self).to_representation(instance)
        data.update({
            'picture': Picture.image,
        })
        return data


class DogDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dog
        fields = ('name', 'blood_type', 'breed', 'current_weight',
                  'age', 'birth_day', 'is_sterize', 'gender',
                  'micro_no', 'color_primary', 'color_secondary',
                  'location', 'dominance', 'dogpicture')

    def to_representation(self, instance):
        data = super(DogDetailSerializer, self).to_representation(instance)
        data.update({
            'vaccination': VaccineRecordSerailizer(VaccineRecord.objects.filter(dog=instance.id), many=True).data,
            'dogpicture': DogPictureSerializer(Picture.objects.filter(dog=instance.id), many=True).data
        })
        return data
