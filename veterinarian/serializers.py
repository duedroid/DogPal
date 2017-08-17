from rest_framework import serializers

from .models import Appointment, Hospital
from dog.models import Dog


class AddAppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = ('hospital', 'dog', 'date', 'status')


class HospitalListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hospital
        fields = ('name',)
