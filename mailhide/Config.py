"""mailhide AppConfig"""
from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class Config(AppConfig):
    """Configuration for mailhide application.

    To include the 'mailhide' application to your project, add this class to
    the INSTALLED_APPS list in Django's settings.
    """
    name = 'mailhide'
    verbose_name = _('Protection e-mails')
