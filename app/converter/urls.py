"""
URLs for converter app.
"""
from django.urls import path

urlpatterns = [
    path('/', views.get_rates, name='rates'),
    path('currencies/', views.currencies_list, name='currencies'),
]
