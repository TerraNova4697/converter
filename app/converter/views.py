"""
Views for Converter APIs.
"""
from django.shortcuts import render


def get_rates(request, currency: str, to: str, value: int = 1):
    """API method to get current rates."""
    if request.method == 'GET':
        pass


def currencies_list(request):
    """API method to get all available currencies."""
    if request.method == 'GET':
        pass
