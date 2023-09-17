"""
Custom exceptions for HTTP requests.
"""
from rest_framework.exceptions import APIException


class ResponseBadRequest(APIException):
    """
    Bad request exception.
    """
    status_code = 400
    default_detail = 'The request is invalid or malformed. Please check the request parameters and try again.'
    default_code = 'service_unavailable'
