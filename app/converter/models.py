"""
Models for converter app.
"""
from django.db import models


class Currency(models.Model):
    title = models.CharField(max_length=255)
    symbol = models.CharField(max_length=55)

    def __str__(self):
        return f'{self.title} ({self.symbol})'
