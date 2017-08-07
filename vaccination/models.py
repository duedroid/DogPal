from django.db import models
from datetime import date

from doginformation.models import Dog
from veterinarian.models import VetHos, Appointment


class VaccinationFor(models.Model):
    name = models.CharField(max_length=100)
    routine = models.CharField(max_length=100)
    note = models.TextField(blank=True)
    vethos = models.ForeignKey(VetHos)
    serial = models.CharField(max_length=100, blank=True, null=True)
    mfg = models.DateField(default=date.today)
    exp = models.DateField(default=date.today)
    appointment = models.ManyToManyField(Appointment, related_name='vaccinationfor')

    timestamp = models.DateTimeField(auto_now_add=True, db_index=True)
    timeupdate = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-timestamp']


class VaccinationRecord(models.Model):
    next_vaccine = models.DateField()
    date_record = models.DateField(default=date.today)
    dog = models.ForeignKey(Dog, related_name='dogvaccine')
    vaccine_for = models.ForeignKey(VaccinationFor, related_name='vaccinationrecord')
    note = models.TextField(blank=True)

    timestamp = models.DateTimeField(auto_now_add=True, db_index=True)
    timeupdate = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-timestamp']
