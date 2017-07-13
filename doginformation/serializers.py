from rest_framework import serializers

from userinformation.models import Profile
from .models import Dog, DogPicture
from veterinarian.models import Appointment, Hospital
from vaccination.models import VaccinationRecord
from vaccination.serializers import VaccinationRecordSerailizer


class DogPictureSerializer(serializers.ModelSerializer):
    class Meta:
        model = DogPicture
        fields = ('id', 'image')


class AddDogSerializer(serializers.ModelSerializer):
    dogpicture = DogPictureSerializer(many=True)

    class Meta:
        model = Dog
        exclude = ('profile', 'timestamp', 'timeupdate',)


class DogDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dog
        exclude = ('profile', 'timestamp', 'timeupdate',)

    def to_representation(self, instance):
        data = super(DogDetailSerializer, self).to_representation(instance)
        data.update({
            'vaccination': VaccinationRecordSerailizer(VaccinationRecord.objects.filter(dog=instance.id), many=True).data,
            'dogpicture': DogPictureSerializer(DogPicture.objects.filter(dog=instance.id), many=True).data
        })
        return data
