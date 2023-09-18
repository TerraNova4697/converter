"""
Views for Converter APIs.
"""
import json

from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import authentication, permissions
from drf_spectacular.utils import (
    extend_schema_view,
    extend_schema,
    OpenApiParameter,
    OpenApiTypes,
)

from converter.models import Currency
from converter.serializers import CurrencySerializer, RatesSerializer
from converter.services.rates_backend.rates_cache import RatesCache
from converter.services.rates_backend.manager import RatesManager
from converter.exceptions.http_exceptions import ResponseBadRequest


@extend_schema_view(
    get=extend_schema(
        parameters=[
            OpenApiParameter(
                'from',
                OpenApiTypes.STR,
                description='Currency that will be converter',
                required=True
            ),
            OpenApiParameter(
                'to',
                OpenApiTypes.STR,
                description='Destination currency',
                required=True
            ),
            OpenApiParameter(
                'value',
                OpenApiTypes.INT,
                description='Amount of currency to be converted',
            ),
        ]
    )
)
class RatesAPIView(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        if 'from' not in request.GET or 'to' not in request.GET:
            raise ResponseBadRequest("Bad request: 'from' and 'to' query parameters are obligatory.")
        if (not isinstance(request.GET.get('from'), str) or
            not isinstance(request.GET.get('to'), str)):
            """Checking parameters are correct."""
            raise ResponseBadRequest("Bad request: wrong query parameters")
        rm = RatesManager(**request.GET)
        try:
            response = rm.get_rates()
        except ValueError as e:
            raise ResponseBadRequest("Bad request: wrong query parameters")
        serializer = RatesSerializer(data=response)

        if serializer.is_valid():
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=400)


class CurrenciesAPIView(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    @method_decorator(cache_page(60*60*2))
    def get(self, request):
        currencies = Currency.objects.all()
        serializer = CurrencySerializer(currencies, many=True)
        return Response(serializer.data)
