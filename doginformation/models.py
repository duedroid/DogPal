from django.db import models
from datetime import date
from userinformation.models import Profile


class Dog(models.Model):
    BLOOD_TYPE_CHOICES = (
        ('A', 'A'),
        ('B', 'B'),
        ('AB', 'AB'),
        ('O', 'O')
    )

    STERIZE_CHOICES = (
        (True, 'Yes'),
        (False, 'No')
    )

    GENDER_CHOICES = (
        (1, 'Male'),
        (2, 'Female')
    )

    name = models.CharField(max_length=200)
    blood_type = models.CharField(max_length=2, choices=BLOOD_TYPE_CHOICES)
    breed = models.CharField(max_length=100)
    current_weight = models.PositiveIntegerField()
    birth_day = models.DateField(default=date.today)
    sterize = models.BooleanField(choices=STERIZE_CHOICES)
    gender = models.PositiveSmallIntegerField(choices=GENDER_CHOICES)
    micro_no = models.IntegerField()
    user = models.ForeignKey(Profile, related_name='dog')
    timestamp = models.DateTimeField(auto_now_add=True, db_index=True)
    timeupdate = models.DateTimeField(auto_now=True)


class DogPicture(models.Model):
    dog = models.ForeignKey(Profile, related_name='dogpicture')
    image = models.ImageField(upload_to='image/%Y/%m/')
    timestamp = models.DateTimeField(auto_now_add=True, db_index=True)
    timeupdate = models.DateTimeField(auto_now=True)

