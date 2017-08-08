from django.db import models
from datetime import date
from dog.models import Dog


class AntiParasitics(models.Model):
    next_dose = models.DateField()
    date_record = models.DateField(default=date.today)
    veterinarian = models.CharField(max_length=100)
    dog = models.ForeignKey(Dog, related_name='antiparasitics')
    note = models.TextField(blank=True)

    timestamp = models.DateTimeField(auto_now_add=True, db_index=True)
    timeupdate = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-timestamp']


class Therapy(models.Model):
    name = models.CharField(max_length=200)
    routine = models.CharField(max_length=200)
    antiparasitics = models.ForeignKey(AntiParasitics, related_name='therapy')
    note = models.TextField(blank=True)

    timestamp = models.DateTimeField(auto_now_add=True, db_index=True)
    timeupdate = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-timestamp']
