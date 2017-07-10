from django.db import models
from datetime import date
from django.contrib.auth.models import User

from doginformation.models import Dog


class Vetarinarian(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    specialties = models.CharField(max_length=100)
    tel = models.CharField(max_length=20)

    timestamp = models.DateTimeField(auto_now_add=True, db_index=True)
    timeupdate = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-timestamp']


class Hospital(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()
    tel = models.CharField(max_length=20)

    timestamp = models.DateTimeField(auto_now_add=True, db_index=True)
    timeupdate = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-timestamp']


class VetHos(models.Model):
    vetarinarian = models.ForeignKey(Vetarinarian, related_name='vet')
    hospital = models.ForeignKey(Hospital, related_name='hos')

    timestamp = models.DateTimeField(auto_now_add=True, db_index=True)
    timeupdate = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-timestamp']


class Appointment(models.Model):
    hospital = models.ForeignKey(Hospital, related_name='appointment_hospital')
    dog = models.ForeignKey(Dog, related_name='appointment_dog')
    date = models.DateField()
    status = models.BooleanField(default=False)

    timestamp = models.DateTimeField(auto_now_add=True, db_index=True)
    timeupdate = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-timestamp']
