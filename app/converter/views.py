"""
Views for Converter APIs.
"""
import json

from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from converter.models import Currency
from converter.serializers import CurrencySerializer, RatesSerializer
from converter.services.rates_backend.rates_api import RatesAPI
from converter.services.rates_backend.manager import RatesManager
from converter.exceptions.http_exceptions import ResponseBadRequest


@api_view(['GET'])
def get_rates(request):
    """API method to get current rates."""
    if request.method == 'GET':
        if 'from' not in request.GET or 'to' not in request.GET:
            return ResponseBadRequest("Bad request: 'from' and 'to' query parameters are obligatory.")
        rm = RatesManager(**request.GET)
        response = rm.get_rates()
        # currency = request.GET.get('from')
        # to = request.GET.get('to')
        # amount = request.GET.get('value', '1')
        # result = RatesAPI().get_rates(currency, to)
        # response = {'result': result}
        serializer = RatesSerializer(data=response)
        if serializer.is_valid():
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=400)


@api_view(['GET'])
def currencies_list(request):
    """API method to get all available currencies."""
    if request.method == 'GET':
        currencies = Currency.objects.all()
        serializer = CurrencySerializer(currencies, many=True)
        return Response(serializer.data)
