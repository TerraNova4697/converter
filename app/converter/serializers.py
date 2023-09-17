"""
Serializers for converter app.
"""
from rest_framework import serializers

from converter.models import Currency


class RatesSerializer(serializers.Serializer):
    """Basic serializer for Rates response."""
    result = serializers.FloatField(min_value=0.000001)
    source = serializers.CharField(max_length=55)


class CurrencySerializer(serializers.ModelSerializer):
    """Basic serializer for Currency object."""

    class Meta:
        model = Currency
        fields = ['title', 'symbol']
