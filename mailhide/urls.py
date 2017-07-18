"""Mailhide URLs"""
from common.api import get_api_urls
from . import api

urlpatterns = [
    get_api_urls(api, 'mailhide'),
]
