from django.db import models


class User(models.Model):
    email = models.CharField(max_length=100)
    login = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    email_is_confirmed = models.BooleanField()
    ip_address = models.CharField(max_length=20)
    date_registration = models.DateTimeField(auto_now=True)


class Date(models.Model):
    date = models.DateTimeField(auto_now=True, blank=True)

    def __str__(self):
        return str(self.date)


class Exchange(models.Model):

    date_refresh = models.ForeignKey(to=Date, on_delete=models.CASCADE)
    fiat = models.CharField(max_length=5)
    asset = models.CharField(max_length=5)
    payment_method = models.CharField(max_length=20)
    price_sell = models.FloatField()
    price_buy = models.FloatField()
