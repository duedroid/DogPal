from rest_framework import serializers

from .models import Appointment, Hospital


class AddAppointmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Appointment
        fields = ('hospital', 'dog', 'date')


class HospitalListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Hospital
        fields = ('id', 'name',)
