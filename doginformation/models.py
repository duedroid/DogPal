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

    name = models.CharField(max_length=200)
    blood_type = models.CharField(max_length=20)
    breed = models.CharField(max_length=100)
    current_weight = models.PositiveSmallIntegerField()
    age = models.PositiveSmallIntegerField()
    birth_day = models.DateField(default=date.today)
    is_sterize = models.BooleanField(choices=STERIZE_CHOICES)
    gender = models.PositiveSmallIntegerField(choices=GENDER_CHOICES)
    micro_no = models.CharField(max_length=100, blank=True, null=True)
    user = models.ForeignKey(Profile, related_name='dog')

    timestamp = models.DateTimeField(auto_now_add=True, db_index=True)
    timeupdate = models.DateTimeField(auto_now=True)


class DogPicture(models.Model):
    dog = models.ForeignKey(Dog, related_name='dogpicture')
    image = models.ImageField(upload_to='image/%Y/%m/')
    
    timestamp = models.DateTimeField(auto_now_add=True, db_index=True)
    timeupdate = models.DateTimeField(auto_now=True)

