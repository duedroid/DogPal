from rest_framework import serializers

from .models import VaccineRecord, VaccineFor, VaccineStockDetail
from veterinarian.models import Appointment


class VaccineRecordSerializer(serializers.ModelSerializer):

    class Meta:
        model = VaccineRecord
        fields = ('id', 'next_vaccine', 'date_record', 'note')


class VaccineRecordBookSerailizer(serializers.ModelSerializer):
    veterinarian = serializers.SerializerMethodField()

    class Meta:
        model = VaccineRecord
        fields = ('id', 'next_vaccine', 'date_record', 'note', 'veterinarian')

    def get_veterinarian(self, vaccinerecord):
        veter = vaccinerecord.veterinarian
        response = {
            'name': veter.first_name + " " + veter.last_name,
            'license': veter.license
        }
        return response


class VaccineStockBookSerializer(serializers.ModelSerializer):

    class Meta:
        model = VaccineFor
        fields = ('id', 'image', 'brand', 'name', 'serial', 'mfg', 'exp')


class RecieveAppointmentSerializer(serializers.Serializer):

    appointment_key = serializers.CharField(max_length=6, required=True)


class VaccineForBookSerializer(serializers.ModelSerializer):
    vaccine_stock_detail = serializers.SerializerMethodField()

    class Meta:
        model = VaccineFor
        fields = ('id', 'name', 'routine', 'note', 'vaccine_stock_detail')

    def get_vaccine_stock_detail(self, vaccinefor):
        vaccinestock = VaccineStockDetail.objects.filter(vaccinefor=instance,
                                                         hospital=self.context['hospital']).first()
        return VaccineStockBookSerializer(vaccinestock, many=True).data
