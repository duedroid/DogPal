from django.db import models
from django.conf import settings
from datetime import date

from dog.models import Dog
from veterinarian.models import VetHos, Appointment, Hospital


class VaccineFor(models.Model):
    name = models.CharField(max_length=255)
    routine = models.CharField(max_length=255)
    note = models.TextField(blank=True)
    appointment = models.ManyToManyField(Appointment, related_name='vaccine_for')

    timestamp = models.DateTimeField(auto_now_add=True, db_index=True)
    timeupdate = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-timestamp']


class VaccineStockDetail(models.Model):
    vaccinefor = models.ForeignKey(VaccineFor, related_name='vaccine_stock_detail')
    hospital = models.ForeignKey(Hospital)
    image = models.ImageField(upload_to='vaccine/%Y/%m/')
    brand = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    serial = models.CharField(max_length=100)
    mfg = models.DateField(default=date.today)
    exp = models.DateField(default=date.today)

    timestamp = models.DateTimeField(auto_now_add=True, db_index=True)
    timeupdate = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-timestamp']



class VaccineRecord(models.Model):
    next_vaccine = models.DateField()
    date_record = models.DateField(default=date.today)
    dog = models.ForeignKey(Dog)
    vaccine_stock = models.ManyToManyField(VaccineStockDetail, related_name='vaccine_record')
    veterinarian = models.ForeignKey(settings.AUTH_USER_MODEL)
    note = models.TextField(blank=True)

    timestamp = models.DateTimeField(auto_now_add=True, db_index=True)
    timeupdate = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-timestamp']
