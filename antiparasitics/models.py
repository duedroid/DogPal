from django.db import models
from datetime import date
from doginformation.models import Dog

class AntiParasitics(models.Model):
    next_dose = models.CharField(max_length=100)
    date_record = models.DateField(default=date.today)
    veterinarian = models.CharField(max_length=100)
    dog = models.ForeignKey(Dog, related_name='antiparasitics')


class Therapy(models.Model):
    name = models.CharField(max_length=200)
    routine = models.CharField(max_length=200)
    antiparasitics = models.ForeignKey(AntiParasitics, related_name='therapy')