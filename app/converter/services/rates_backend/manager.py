"""
Management class for rates operations.
"""
from converter.services.rates_backend.rates_api import RatesAPI
# from converter.services.rates_backend.rates_api import RatesAPI


class RatesManager:

    def __init__(self, **kwargs):
        self.currency = kwargs.get('from')[0]
        self.to = kwargs.get('to')[0]
        self.amount = int(kwargs.get('value', '1')[0])
        self.api_class = RatesAPI()

    def get_rates(self):
        """returns dict {'result': amount} for particular currencies."""
        # if in cache get cached value
        # else
        value = float(self.api_class.get_rates(self.currency, self.to))
        result = self._format_float(self.amount * value)
        return {'result': result}

    def _format_float(self, value):
        """Round float value to maximum 4 digits after trailing coma and return value."""
        if len(str(value).split('.')[1]) > 4:
            return round(value, 4)
        return value
