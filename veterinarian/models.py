from django.db import models
from datetime import date
from django.conf import settings

from dog.models import Dog


class Hospital(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()
    tel = models.CharField(max_length=20)

    timestamp = models.DateTimeField(auto_now_add=True, db_index=True)
    timeupdate = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-timestamp']


class VetHos(models.Model):
    vetarinarian = models.ForeignKey(settings.AUTH_USER_MODEL)
    hospital = models.ForeignKey(Hospital, related_name='vethos')

    timestamp = models.DateTimeField(auto_now_add=True, db_index=True)
    timeupdate = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-timestamp']


class Appointment(models.Model):
    hospital = models.ForeignKey(Hospital, related_name='appointment_hospital')
    dog = models.ForeignKey(Dog, related_name='appointment_dog')
    date = models.DateField()
    status = models.BooleanField(default=True)
    is_overdate = models.BooleanField(default=False)

    timestamp = models.DateTimeField(auto_now_add=True, db_index=True)
    timeupdate = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-timestamp']

    def toggle_is_overdate(self):
        self.is_overdate = True
        self.save()
