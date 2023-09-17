"""
Models for converter app.
"""
from django.db import models


class Currency(models.Model):
    """
    Currency model.

    Attributes:
        title (str): full name of a currency.
        symbol (str): short abbriviation of a currency.
    """
    title = models.CharField(max_length=255)
    symbol = models.CharField(max_length=55)

    def __str__(self):
        """
        String representation.
        """
        return f'{self.title} ({self.symbol})'
