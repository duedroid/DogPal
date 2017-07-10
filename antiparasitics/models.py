from django.db import models
from datetime import date
from doginformation.models import Dog

class AntiParasitics(models.Model):
    next_dose = models.DateField()
    date_record = models.DateField(default=date.today)
    veterinarian = models.CharField(max_length=100)
    dog = models.ForeignKey(Dog)
    note = models.TextField(blank=True)

    timestamp = models.DateTimeField(auto_now_add=True, db_index=True)
    timeupdate = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-timestamp']


class Therapy(models.Model):
    name = models.CharField(max_length=200)
    routine = models.CharField(max_length=200)
    antiparasitics = models.ForeignKey(AntiParasitics)
    note = models.TextField(blank=True)

    timestamp = models.DateTimeField(auto_now_add=True, db_index=True)
    timeupdate = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-timestamp']
