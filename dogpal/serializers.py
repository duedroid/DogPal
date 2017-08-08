from rest_framework import serializers

from account.models import Account
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
            'dogpicture': DogPictureSerializer(DogPicture.objects.get(dog=instance.id)).data
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
            'hospital': HospitalSerializer(Hospital.objects.get(id=instance.hospital_id)).data,
            'dog': DogListSerializer(Dog.objects.get(id=instance.dog_id)).data
        })
        return data


class HomeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Dog
        fields = ('id', 'name', 'dogpicture',)

    def to_representation(self, instance):
        data = super(HomeSerializer, self).to_representation(instance)
        data.update({
            'appointment': AppointmentSerializer(Appointment.objects.filter(status=True), many=True).data,
            'picture': DogPictureSerializer(many=True, read_only=True).data
        })
        return data
