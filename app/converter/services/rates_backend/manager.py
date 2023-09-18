"""
Management class for rates operations.
"""
from converter.services.rates_backend.rates_api import RatesAPI
from converter.services.rates_backend.rates_cache import RatesCache


class RatesManager:
    """
    Management class for rates. Determines where to fetch data from.
    """

    def __init__(self, **kwargs):
        """
        Initialization function.

        Args:
            kwargs (dict): possible keys - from, to, value.
        """
        self.currency = kwargs.get('from', ['USD'])[0]
        self.to = kwargs.get('to', ['RUB'])[0]
        self.amount = int(kwargs.get('value', '1')[0])
        self.api = RatesAPI()
        self.cache = RatesCache()

    def get_rates(self):
        """
        Fetches rates.

        Returns:
            dict for particular currencies.
        """
        value = self.cache.get_rates(f'{self.currency}{self.to}')
        rate = {}
        if value:
            value = float(value)
            rate['source'] = 'cache'
        else:
            response = self.api.get_rates(self.currency, self.to)
            self.cache.save_rates(f'{self.currency}{self.to}', response)
            value = float(response)
            rate['source'] = 'api'

        result = self._format_float(self.amount * value)
        rate['result'] = result
        return rate

    def _format_float(self, value):
        """
        Round float value to maximum 4 digits after trailing coma and return value.

        Returns:
            float formatted.
        """
        if len(str(value).split('.')[1]) > 4:
            return round(value, 4)
        return value
