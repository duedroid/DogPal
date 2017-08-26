from django.db import models
from datetime import date
from django.conf import settings


class Dog(models.Model):
    STERIZE_CHOICES = (
        (True, 'Yes'),
        (False, 'No')
    )

    GENDER_CHOICES = (
        (1, 'Male'),
        (2, 'Female')
    )

    STATUS_CHOICES = (
        (1, 'Alive'),
        (2, 'Death')
    )

    account = models.ForeignKey(settings.AUTH_USER_MODEL)
    name = models.CharField(max_length=200)
    blood_type = models.CharField(max_length=20)
    breed = models.CharField(max_length=100)
    current_weight = models.PositiveSmallIntegerField()
    age = models.PositiveSmallIntegerField(blank=True, null=True)
    birth_day = models.DateField(default=date.today)
    is_sterize = models.BooleanField(choices=STERIZE_CHOICES)
    gender = models.PositiveSmallIntegerField(choices=GENDER_CHOICES)
    micro_no = models.CharField(max_length=100, blank=True, null=True)
    color_primary = models.CharField(max_length=20, blank=True, null=True)
    color_secondary = models.CharField(max_length=20, blank=True, null=True)
    location = models.TextField()
    dominance = models.CharField(max_length=200)
    status = models.PositiveSmallIntegerField(choices=STATUS_CHOICES, default=1)

    timestamp = models.DateTimeField(auto_now_add=True, db_index=True)
    timeupdate = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-timestamp']

    def __str__(self):
        return self.name


class Picture(models.Model):
    dog = models.ForeignKey(Dog, related_name='picture', blank=True, null=True)
    image = models.ImageField(upload_to='dog_image/%Y/%m/')
    vector = models.CharField(max_length=100, blank=True, null=True)

    timestamp = models.DateTimeField(auto_now_add=True, db_index=True)
    timeupdate = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-timestamp']

