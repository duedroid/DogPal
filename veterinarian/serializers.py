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


class SearchAppointmentSerializer(serializers.Serializer):

    search = serializers.CharField(min_length=1, required=True)
    hospital_id = serializers.IntegerField(required=True)


class AppointmentResultSerializer(serializers.ModelSerializer):
    dog = serializers.SerializerMethodField()
    account_name = serializers.SerializerMethodField()

    class Meta:
        model = Appointment
        fields = ('key', 'dog', 'account_name')

    def get_dog(self, appointment):
        return appointment.dog.name

    def get_account_name(self, appointment):
        return appointment.dog.account.first_name + " " + appointment.dog.account.last_name
