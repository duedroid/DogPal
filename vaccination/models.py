from django.db import models
from datetime import date
from doginformation.models import Dog

class VaccinationFor(models.Model):
    name = models.CharField(max_length=100)
    routine = models.CharField(max_length=100)

class VaccinationRecord(models.Model):
    veternarian = models.CharField(max_length=100)
    next_vaccine = models.CharField(max_length=100)
    date_record = models.DateField(default=date.today)
    dog = models.ForeignKey(Dog, related_name='dogvaccine')
    vaccine_for = models.ForeignKey(VaccinationFor, related_name='vaccinationrecord')