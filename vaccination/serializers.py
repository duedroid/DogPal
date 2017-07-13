from rest_framework import serializers

from vaccination.models import VaccinationRecord

class VaccinationRecordSerailizer(serializers.ModelSerializer):
    class Meta:
        model = VaccinationRecord
        fields = ('id', 'next_vaccine', 'date_record', 'note')
