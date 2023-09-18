"""
URLs for converter app.
"""
from django.urls import path
from converter import views

app_name = 'converter'

urlpatterns = [
    path('', views.RatesAPIView.as_view(), name='rates'),
    path('currencies', views.CurrenciesAPIView.as_view(), name='currencies'),
]
