from django.db import models
from django.conf import settings
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser, PermissionsMixin, Permission)
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _


class ProfileManager(BaseUserManager):

    def _create_user(self, email, set_password, is_veterinarian,
                     **extra_fields):
        if not email:
            raise ValueError(_('The given email must be set'))

        user = self.model(
            email=self.normalize_email(email),
            is_veterinarian=is_veterinarian,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        return self._create_user(email,
                                 password=password,
                                 is_veterinarian=False,
                                 **extra_fields)

    def create_veterinarian(self, email, password=None, **extra_fields):
        return self._create_user(email,
                                 password=password,
                                 is_veterinarian=True,
                                 **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        user = self._create_user(email,
                                 password=password,
                                 is_veterinarian=False,
                                 **extra_fields)
        user.is_admin = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class Profile(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        verbose_name='Email address',
        max_length=255,
        unique=True,
    )

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    tel_1 = models.CharField(max_length=20)
    tel_2 = models.CharField(max_length=20, blank=True)

    latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    longtitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)

    address = models.TextField(max_length=200)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=10)

    is_admin = models.BooleanField(default=False)
    is_veterinarian = models.BooleanField(default=False)

    specialties = models.CharField(max_length=100, null=True, blank=True)

    last_active = models.DateTimeField(_('last active'), blank=True, null=True)
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)

    objects = ProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
