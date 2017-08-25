from rest_framework import serializers

from dog.models import Dog, Picture
from veterinarian.models import Appointment, Hospital
from dog.serializers import DogListSerializer


class HospitalSerializer(serializers.ModelSerializer):

    class Meta:
        model = Hospital
        fields = ('id', 'name',)


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
    appointment = serializers.SerializerMethodField()

    class Meta:
        model = Dog
        fields = ('appointment',)

    def get_appointment(self, dog):
        appointment = Appointment.objects.filter(status=True, dog=dog)
        if not appointment:
            return None

        from datetime import datetime, timedelta

        for obj in appointment:
            if obj.date <= datetime.now().date() + timedelta(days=1):
                obj.is_overdate = True
                obj.save()
        return AppointmentSerializer(appointment, many=True).data
