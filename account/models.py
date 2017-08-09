from django.db import models
from django.conf import settings
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser, PermissionsMixin, Permission)
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _


class AccountManager(BaseUserManager):

    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError(_('The given email must be set'))
        now = timezone.now()
        user = self.model(
            email=self.normalize_email(email),
            last_active=now,
            date_joined=now,
            is_active=True,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        return self._create_user(email=email,
                                 password=password,
                                 **extra_fields)

    def create_veterinarian(self, email, password=None, **extra_fields):
        user = self._create_user(email=email,
                                 password=password,
                                 **extra_fields)
        user.is_veterinarian = True
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        user = self._create_user(email=email,
                                 password=password,
                                 **extra_fields)
        user.is_admin = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class Account(AbstractBaseUser, PermissionsMixin):
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

    address = models.TextField(max_length=255)
    city = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=10)

    is_admin = models.BooleanField(default=False)
    is_veterinarian = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    specialties = models.CharField(max_length=100, null=True, blank=True)

    last_active = models.DateTimeField(_('last active'), blank=True, null=True)
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)

    objects = AccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    @property
    def is_staff(self):
        return self.is_admin

    def get_short_name(self):
        return self.email

    def get_full_name(self):
        return '{0} {1}'.format(self.first_name, self.last_name)
