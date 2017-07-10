from django.db import models
from datetime import date
from userinformation.models import Profile


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

    profile = models.ForeignKey(Profile, related_name='dog')
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
    location = models.TextField(max_length=300)
    dominance = models.CharField(max_length=200)
    status = models.PositiveSmallIntegerField(choices=STATUS_CHOICES)

    timestamp = models.DateTimeField(auto_now_add=True, db_index=True)
    timeupdate = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-timestamp']


class DogPicture(models.Model):
    dog = models.ForeignKey(Dog, related_name='dogpicture', blank=True, null=True)
    image = models.ImageField(upload_to='image/%Y/%m/')
    vector = models.CharField(max_length=100, blank=True, null=True)

    timestamp = models.DateTimeField(auto_now_add=True, db_index=True)
    timeupdate = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-timestamp']

