"""
Views for Converter APIs.
"""
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from converter.models import Currency
from converter.serializers import CurrencySerializer


def get_rates(request, currency: str, to: str, value: int = 1):
    """API method to get current rates."""
    if request.method == 'GET':
        pass


@api_view(['GET'])
def currencies_list(request):
    """API method to get all available currencies."""
    if request.method == 'GET':
        currencies = Currency.objects.all()
        serializer = CurrencySerializer(currencies, many=True)
        return Response(serializer.data)
