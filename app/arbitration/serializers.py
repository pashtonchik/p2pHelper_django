from rest_framework import serializers
from .models import *


class DateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Date
        exclude = ('date', )


class ExchangeSerializer(serializers.ModelSerializer):
    date_refresh = DateSerializer()

    class Meta:
        model = Exchange
        fields = '__all__'
