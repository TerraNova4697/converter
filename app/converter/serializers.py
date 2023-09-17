"""
Serializers for converter app.
"""
from rest_framework import serializers

from converter.models import Currency


class CurrencySerializer(serializers.ModelSerializer):
    """Basic serializer for Currency object."""

    class Meta:
        model = Currency
        fields = ['title', 'symbol']
