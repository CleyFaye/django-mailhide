"""Mailhide URLs.

Import this module into your application's URLs using include() and the
'mailhide' prefix/namespace.
"""
from django.conf.urls import (url,
                              include)
from tastypie.api import NamespacedApi
from .api import MailResource

api_urls = NamespacedApi(api_name='v1', urlconf_namespace='mailhide')
api_urls.register(MailResource())

urlpatterns = [
    url(r'^api/', include(api_urls.urls))
]
