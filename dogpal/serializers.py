from rest_framework import serializers

from dog.models import Dog, Picture
from veterinarian.models import Appointment, Hospital
from dog.serializers import DogListSerializer


class AppointmentSerializer(serializers.ModelSerializer):
    hospital = serializers.SerializerMethodField()
    dog = serializers.SerializerMethodField()

    class Meta:
        model = Appointment
        fields = ('id', 'date', 'is_overdate', 'hospital', 'dog')

    def get_hospital(self, appointment):
        return appointment.hospital.name

    def get_dog(self, appointment):
        return DogListSerializer(appointment.dog).data


class HomeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Dog
        fields = ()

    def to_representation(self, instance):
        appointment = Appointment.objects.filter(status=True, dog=instance).order_by('-date')
        if not appointment:
            return None

        from datetime import datetime, timedelta

        for obj in appointment:
            if obj.date < datetime.now().date() + timedelta(days=1):
                obj.is_overdate = True
                obj.save(update_fields=['is_overdate'])

        return AppointmentSerializer(appointment, many=True).data
