"""mailhide AppConfig"""
from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class Config(AppConfig):
    """Configuration for mailhide application."""
    name = 'mailhide'
    verbose_name = _('Protection e-mails')
