"""API for fetching an e-mail"""
from tastypie.resources import NamespacedModelResource
from tastypie.authentication import Authentication
from tastypie.cache import NoCache
from pycaptcha.django import TastypieAuthorization
from mailhide.models import Mailhide


class MailResource(NamespacedModelResource):
    """Return an e-mail from the DB.

    Notes
    -----
    This will only return a reply if a reCAPTCHA challenge is provided.
    """
    class Meta:
        queryset = Mailhide.objects.all()
        allowed_methods = []
        list_allowed_methods = ['get']
        authentication = Authentication()
        authorization = TastypieAuthorization()
        filtering = {'key': ('exact',)}
        fields = ['address']
        cache = NoCache()
