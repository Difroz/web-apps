import csv
import io
from datetime import datetime

from rest_framework import serializers

from .models import Deal


class InfoSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=200)
    spend_money = serializers.DecimalField(max_digits=10, decimal_places=2)
    gems = serializers.ListField()

    class Meta:
        fields = ('username', 'spend_money', 'gems')


class UploadSerializer(serializers.Serializer):
    deals = serializers.FileField()

    class Meta:
        fields = ('deals')







