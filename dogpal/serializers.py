from rest_framework import serializers

from dog.models import Dog, Picture
from veterinarian.models import Appointment, Hospital
from dog.serializers import DogPictureSerializer


class DogListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Dog
        fields = ('id', 'name',)

    def to_representation(self, instance):
        data = super(DogListSerializer, self).to_representation(instance)
        data.update({
            'dogpicture': DogPictureSerializer(Picture.objects.filter(dog=instance.id).first()).data
        })
        return data


class HospitalSerializer(serializers.ModelSerializer):

    class Meta:
        model = Hospital
        fields = ('id', 'name',)


class AppointmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Appointment
        fields = ('id', 'date', 'is_overdate')

    def to_representation(self, instance):
        data = super(AppointmentSerializer, self).to_representation(instance)
        data.update({
            'hospital': instance.hospital.name,
            'dog': DogListSerializer(instance.dog).data
        })
        return data


class HomeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Dog
        fields = ()

    def to_representation(self, instance):
        data = super(HomeSerializer, self).to_representation(instance)
        dog = Dog.objects.filter(id=instance.id)
        data.update({
            'dog': DogListSerializer(dog, many=True).data,
            'appointment': AppointmentSerializer(Appointment.objects.filter(status=True, dog=dog), many=True).data,
        })
        return data
