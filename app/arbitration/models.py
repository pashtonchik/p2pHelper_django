from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.utils import timezone

from .managers import CustomUserManager


class Client(AbstractBaseUser, PermissionsMixin):
    email = models.CharField(max_length=100)
    login = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    tg_link = models.CharField(max_length=100)
    email_is_confirmed = models.BooleanField(default=False)
    date_registration = models.DateTimeField(default=timezone.now)
    is_paid_subscription = models.BooleanField(default=False)
    sub_time_begin = models.DateTimeField(blank=True, null=True)
    sub_time_end = models.DateTimeField(blank=True, null=True)
    sub_time_days = models.IntegerField(default=0)

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'login'
    REQUIRED_FIELDS = ['password', 'email']

    objects = CustomUserManager()

    def __str__(self):
        return self.login


class Date(models.Model):
    date = models.DateTimeField(auto_now=True, blank=True)

    def __str__(self):
        return str(self.date)


class Exchange(models.Model):

    date_refresh = models.ForeignKey(to=Date, on_delete=models.CASCADE)
    fiat = models.CharField(max_length=5)
    asset = models.CharField(max_length=5)
    payment_method = models.CharField(max_length=20)
    price = models.FloatField()
