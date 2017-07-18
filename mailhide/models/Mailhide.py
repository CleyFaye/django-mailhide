"""Class for managing mailhide association"""
from math import floor
from random import random
from django.utils.translation import ugettext as _
from django.db import (models,
                       IntegrityError)


MODEL_NAME = _('Adresse mailhide')
MODEL_NAME_PLURAL = _('Adresses mailhide')

FIELD_ADDRESS_VERBOSE = _('Adresse réelle')
FIELD_ADDRESS_HELP = _('Adresse non modifié d\'origine')
FIELD_KEY_VERBOSE = _('Clé')
FIELD_KEY_HELP = _('Clé correspondante au mail')


class Mailhide(models.Model):
    """An email address protected using reCAPTCHA.

    Fields
    ------
    address : models.CharField
        The e-mail address to protect
    key : models.CharField
        The key to identify the e-mail address
    """
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
                           max_length=10,
                           null=False,
                           blank=False,
                           unique=True)

    def __str__(self):
        return '%s' % self.address

    @classmethod
    def get(cls, address):
        """Return an instance of Mailhide for the given address.

        Parameters
        ----------
        address : string
            The e-mail address to protect.


        Returns
        -------
        Mailhide
            An instance of Mailhide representing the entry

        Notes
        -----
        If an existing entry is available, it is returned. Otherwise a new entry
        is created and returned.
        """
        try:
            return cls.objects.get(address=address)
        except cls.DoesNotExist:
            pass
        # This is a safeguard, but should never happen
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
