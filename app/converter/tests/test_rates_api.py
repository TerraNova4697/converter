"""
Test for the rates API.
"""
from django.urls import reverse
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient

from converter.serializers import RatesSerializer
from converter.services.rates_backend.rates_cache import RatesCache
from converter.models import Currency
from converter.serializers import CurrencySerializer


RATES_URL = reverse('converter:rates')
CURRENCIES_URL = reverse('converter:currencies')


class RatesApiTests(TestCase):
    """Tests for 'converter:rates' route API."""

    def setUp(self):
        self.client = APIClient()
        self.redis = RatesCache()

    def test_retrieve_rate(self):
        """Test retrieving simple rate."""
        res = self.client.get(RATES_URL, data={'from': 'USD', 'to': 'EUR'})

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertContains(res, 'result')
        self.assertTrue(isinstance(res.data['result'], float))

    def test_requested_rates_cached(self):
        """Test requested currencies are cached."""
        self.redis.flush_db()
        res = self.client.get(RATES_URL, data={'from': 'USD', 'to': 'EUR'})

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertTrue(res.data['source'] == 'api')

        res2 = self.client.get(RATES_URL, data={'from': 'USD', 'to': 'EUR'})
        self.assertEqual(res2.status_code, status.HTTP_200_OK)
        self.assertTrue(res2.data['source'] == 'cache')

    def test_required_query_parameters_exist(self):
        """Test all required parameters are passed to URL query."""
        res = self.client.get(RATES_URL, data={'from': 'USD'})

        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_passed_correct_parameters(self):
        """Test all query parameters are correct."""
        res = self.client.get(RATES_URL, data={'from': 1, 'to': 'USD'})

        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
