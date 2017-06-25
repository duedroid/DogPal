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

class Hospital(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()
    tel = models.CharField(max_length=20)

    timestamp = models.DateTimeField(auto_now_add=True, db_index=True)
    timeupdate = models.DateTimeField(auto_now=True)

class VetHos(models.Model):
    vetarinarian = models.ForeignKey(Vetarinarian)
    hospital = models.ForeignKey(Hospital)

class Appointment(models.Model):
    hospital = models.ForeignKey(Hospital)
    dog = models.ForeignKey(Dog)
    date = models.DateField()
    status = models.BooleanField(default=False)