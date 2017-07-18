"""Provide the mailhide tag"""
from urllib.parse import quote
from django import template
from django.conf import settings
from django.utils.safestring import mark_safe
from mailhide.models import Mailhide
register = template.Library()


MAILHIDE_DIV_KEY = 'mailhide_div_ok'


@register.simple_tag(takes_context=True)
def mailhide(context, address, subject=''):
    """Return the mailhide block for an email address.

    Parameters
    ----------
    context : Context
        The template context (automatically passed when using a template tag)
    address : string
        The e-mail address to protect
    subject : string (optional)
        The e-mail subject when a user click on the link


    Returns
    -------
    string
        The appropriate elements to display a clickable link that allow users to
        send an e-mail.


    Notes
    -----
    E-mail addresses not present in the database will be automatically added.
    The returned block will contain a special <span> element the first time it
    is called, need for reCAPTCHA to operate correctly.

    Other than that, the link will have the form "p…@domain" and, when clicked,
    will open a mailing agent with the appropriate address.
    """
    address = str(address)
    subject = str(subject)
    entry = Mailhide.get(address)
    recipient, domain = address.split('@')
    if MAILHIDE_DIV_KEY in context and context[MAILHIDE_DIV_KEY]:
        result_div = ''
    else:
        result_div = ('<span data-sitekey="%(apikey)s"'
                      + ' class="g-recaptcha"'
                      + ' data-callback="mailhide_cb"'
                      + ' style="display: none"'
                      + ' data-size="invisible"></span>') % {
                          'apikey': settings.RECAPTCHA_API_KEY}
        context[MAILHIDE_DIV_KEY] = True
    result_link = ('<a data-mailkey="%(k)s"'
                   + ' data-subject="%(subject)s"'
                   + '>%(firstletter)s…@%(domain)s</a>') % {
                       'k': entry.key,
                       'subject': quote(subject),
                       'firstletter': recipient[0],
                       'domain': domain}
    return mark_safe(result_div + result_link)
