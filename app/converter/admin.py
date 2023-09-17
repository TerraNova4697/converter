"""
Django admin customization.
"""
from django.contrib import admin

from converter import models


class CurrencyAdmin(admin.ModelAdmin):
    """
    Customize admin page for Currency model.
    """
    ordering = ['id']
    list_display = ['title', 'symbol']


admin.site.register(models.Currency, CurrencyAdmin)
