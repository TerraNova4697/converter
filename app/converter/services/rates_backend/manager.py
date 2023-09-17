"""
Management class for rates operations.
"""
from converter.services.rates_backend.rates_api import RatesAPI
from converter.services.rates_backend.rates_cache import RatesCache


class RatesManager:

    def __init__(self, **kwargs):
        self.currency = kwargs.get('from')[0]
        self.to = kwargs.get('to')[0]
        self.amount = int(kwargs.get('value', '1')[0])
        self.api = RatesAPI()
        self.cache = RatesCache()

    def get_rates(self):
        """returns dict {'result': amount} for particular currencies."""
        value = self.cache.get_rates(f'{self.currency}{self.to}') 
        print(value)
        if value:
            value = float(value)
            print('FROM CACHE', value)
        else:
            response = self.api.get_rates(self.currency, self.to)
            self.cache.save_rates(f'{self.currency}{self.to}', response)
            value = float(response)
            print('FROM API', value)

        result = self._format_float(self.amount * value)
        return {'result': result}

    def _format_float(self, value):
        """Round float value to maximum 4 digits after trailing coma and return value."""
        if len(str(value).split('.')[1]) > 4:
            return round(value, 4)
        return value
