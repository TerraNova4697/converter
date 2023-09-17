"""
Backend for getting rates from the external API.
"""
import requests
from requests.exceptions import HTTPError, Timeout

from converter.services.rates_backend.rates_source import RatesSource

BASE_URL = 'https://api.coingate.com/api/v2'


class RatesAPI(RatesSource):
    """Fetching rates from API."""

    def _base_request(self, **kwargs):
        """Base method for API request."""
        req_type = kwargs.get('req_type')

        if req_type == 'get':
            request_url = BASE_URL + kwargs.get('endpoint')
            headers = {"accept": "text/plain"}

            params = kwargs.get('params')
            if params:
                request_url = request_url + params

            try:
                response = requests.get(url=request_url, headers=headers)
                return response.text
            except (HTTPError, Timeout) as e:
                # TODO: log exceptions
                print(e)

    def get_rates(self, currency: str, to: str):
        """Fetching rates for one currency compared to another from external API."""
        endpoint = f'/rates/merchant/{currency}/{to}'
        return self._base_request(req_type='get', endpoint=endpoint)

    def _get_api_key(self):
        """Return api key needed for API request."""
        pass
