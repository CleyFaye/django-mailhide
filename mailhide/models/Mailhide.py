"""Class for managing mailhide association"""
from logging import getLogger
from math import floor
from random import random
from django.utils.translation import ugettext as _
from django.db import (models,
                       IntegrityError)
logg = getLogger(__name__)


MODEL_NAME = _('Adresse mailhide')
MODEL_NAME_PLURAL = _('Adresses mailhide')

FIELD_ADDRESS_VERBOSE = _('Adresse réelle')
FIELD_ADDRESS_HELP = _('Adresse non modifié d\'origine')
FIELD_KEY_VERBOSE = _('Clé')
FIELD_KEY_HELP = _('Clé correspondante au mail')


class Mailhide(models.Model):
    """An email address protected using reCAPTCHA."""
    class Meta:
        app_label = 'mailhide'
        ordering = ['address']
        verbose_name = MODEL_NAME
        verbose_name_plural = MODEL_NAME_PLURAL

    KEY_SYMBOLS = 'ABCDEFGHJKMNPQRTUVWXY234578'

    address = models.CharField(verbose_name=FIELD_ADDRESS_VERBOSE,
                               help_text=FIELD_ADDRESS_HELP,
                               max_length=500,
                               null=False,
                               blank=False,
                               unique=True)
    key = models.CharField(verbose_name=FIELD_KEY_VERBOSE,
                           help_text=FIELD_KEY_HELP,
                           max_length=100,
                           null=False,
                           blank=False,
                           unique=True)

    def __str__(self):
        return '%s' % self.address

    @classmethod
    def create(cls, address):
        iterations_left = 100
        while True:
            key = ''.join([
                cls.KEY_SYMBOLS[floor(random() * len(cls.KEY_SYMBOLS))]
                for _ in range(6)])
            try:
                result = cls(address=address, key=key)
                result.save()
                return result
            except IntegrityError:
                iterations_left -= 1
                if not iterations_left:
                    raise
