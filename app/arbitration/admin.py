from django.contrib import admin
from .models import *


@admin.register(MyUser)
class ExchangeAdmin(admin.ModelAdmin):
    list_display = ('email', 'login', 'is_paid_subscription')


@admin.register(Exchange)
class ExchangeAdmin(admin.ModelAdmin):
    list_display = ('fiat', 'asset', 'payment_method', 'price_sell', 'price_buy', 'date_refresh')


@admin.register(Date)
class DateAdmin(admin.ModelAdmin):
    list_display = ('date', )
