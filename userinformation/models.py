from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    tel_1 = models.CharField(max_length=20)
    tel_2 = models.CharField(max_length=20, blank=True)
    address = models.TextField(max_length=300)
    lineid = models.CharField(max_length=50)
    facebook = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True, db_index=True)
    timeupdate = models.DateTimeField(auto_now=True)
