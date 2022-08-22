from django.contrib import admin
from .models import *


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('login', 'email', 'is_paid_subscription')
    fields = ('login', 'email', 'email_is_confirmed', 'date_registration', 'is_paid_subscription',
              'sub_time_begin', 'sub_time_end', 'sub_time_days')
    readonly_fields = ('login', 'email', 'date_registration')


@admin.register(Exchange)
class ExchangeAdmin(admin.ModelAdmin):
    list_display = ('fiat', 'asset', 'payment_method', 'price', 'date_refresh')


@admin.register(Date)
class DateAdmin(admin.ModelAdmin):
    list_display = ('date', )
