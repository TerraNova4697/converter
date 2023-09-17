"""
Redis cache class for caching rates.
"""
import redis

from converter.services.rates_backend.rates_source import RatesSource
from converter.services.singleton import Singleton


class RatesCache(Singleton, RatesSource):
    """Redis chache class."""

    def __init__(self):
        self._redis = redis.Redis(
            host='cache',
            password='eYVX7EwVmmxKPCDmwMtyKVge8oLd2t81'
        )

    def get_rates(self, key: str):
        """Returns string representation of rates if exists in cache and still valid. Otherwise returns None."""
        return self._redis.get(key)

    def save_rates(self, key: str, value: str):
        """Saves given currencies as a key and its rates as value for one hour."""
        hour_in_sec = 60*60*60
        self._redis.set(name=key, value=value, ex=hour_in_sec)
