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

    def __str__(self):
        return self.name


class VetHos(models.Model):
    vetarinarian = models.ForeignKey(settings.AUTH_USER_MODEL)
    hospital = models.ForeignKey(Hospital)

    timestamp = models.DateTimeField(auto_now_add=True, db_index=True)
    timeupdate = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-timestamp']


class Appointment(models.Model):
    key = models.CharField(max_length=6, null=True, blank=True, unique=True)
    hospital = models.ForeignKey(Hospital, related_name='appointment_hospital')
    dog = models.ForeignKey(Dog, related_name='appointment_dog')
    date = models.DateField()
    status = models.BooleanField(default=True)
    is_overdate = models.BooleanField(default=False)

    timestamp = models.DateTimeField(auto_now_add=True, db_index=True)
    timeupdate = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-timestamp']

    def __str__(self):
        return self.key

    def save(self, **kwargs):
        if not self.key:
            self.key = generate_key()
            while Appointment.objects.filter(key=self.key).exists():
                self.key = generate_key()
        super(Appointment, self).save()


def generate_key():
        import random
        import string

        return ''.join(random.sample(string.ascii_letters+string.digits, 6))
