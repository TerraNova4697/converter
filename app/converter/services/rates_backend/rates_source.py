"""
Abstract method for Rates source.
"""

from abc import ABC, abstractmethod


class RatesSource(ABC):

    @abstractmethod
    def get_rates(self, currency: str, to: str):
        pass
