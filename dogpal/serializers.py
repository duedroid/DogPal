from rest_framework import serializers

from userinformation.models import Profile
from doginformation.models import Dog, DogPicture
from veterinarian.models import Appointment, Hospital


class DogPictureSerializer(serializers.ModelSerializer):
    class Meta:
        model = DogPicture
        fields = ('id', 'image')


class DogListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dog
        fields = ('name',)

    def to_representation(self, instance):
        data = super(DogListSerializer, self).to_representation(instance)
        data.update({
            'dogpicture': DogPictureSerializer(DogPicture.objects.get(dog=instance.id)).data
        })
        return data


class HospitalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hospital
        fields = ('name',)


class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = ('date', 'hospital', 'dog')

    def to_representation(self, instance):
        data = super(AppointmentSerializer, self).to_representation(instance)
        data.update({
            'hospital': HospitalSerializer(Hospital.objects.get(id=instance.hospital_id)).data,
            'dog': DogListSerializer(Dog.objects.get(id=instance.dog_id)).data
        })
        return data


class HomeSerializer(serializers.ModelSerializer):
    dog = DogListSerializer(many=True, read_only=True)

    class Meta:
        model = Profile
        fields = ('id', 'dog',)

    def to_representation(self, instance):
        data = super(HomeSerializer, self).to_representation(instance)
        data.update({
            'appointment': AppointmentSerializer(Appointment.objects.filter(status=True), many=True).data
        })
        return data
