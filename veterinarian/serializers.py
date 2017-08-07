from rest_framework import serializers

from .models import Appointment


class AddAppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = ('id', 'hospital', 'dog', 'date', 'status')
