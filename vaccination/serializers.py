from rest_framework import serializers

from vaccination.models import VaccineRecord

class VaccineRecordSerailizer(serializers.ModelSerializer):
    class Meta:
        model = VaccineRecord
        fields = ('id', 'next_vaccine', 'date_record', 'note')
