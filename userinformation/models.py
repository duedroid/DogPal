from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    tel_1 = models.CharField(max_length=20)
    tel_2 = models.CharField(max_length=20, blank=True)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    longtitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    address = models.TextField(max_length=200)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=10)

    timestamp = models.DateTimeField(auto_now_add=True, db_index=True)
    timeupdate = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-timestamp']
