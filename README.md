Django-mailhide
===============

The mailhide application allow easy protection of e-mail addresses using reCAPTCHA.

This package is not endorsed by the Django team in any way.


Prerequisites
-------------
To perform server-side checks, the [pycaptcha](https://repos.cleyfaye.net/trac/pycaptcha) library is used.
It also requires a valid reCAPTCHA API key.


Installation and Configuration
------------------------------
You must insert the mailhide application as you would any other Django application, in the INSTALLED\_APPS property:

    INSTALLED\_APPS = [some.apps,
                       mailhide.MailHideConfig,
                       some.other.apps]

Also set the reCAPTCHA API key and shared secret in Django settings (properties RECAPTCHA\_API\_KEY and RECAPTCHA\_SHARED\_SECRET).

Finally, add the mailhide.urls module to your list of URLs (usually using include() from Django).
The Javascript expect to find the API at the following address: "/mailhide/api/v1/mail", so your include must use the "mailhide" prefix.

This project assume that the static files in "mailhide/static" will get collected (for example using "manage.py collectstatic") and that the template will be looked up in "mailhide/templates".
If that's not the case, you'll have to copy the file were appropriate.

Usage
-----
In each page that will use mailhide, you must import the reCAPTCHA Javascript and the mailhide Javascript.
This can be done by including templates "inc/recaptcha.html" and "inc/mailhide.html" in your HTML header.

To use the tag, import the "mailhide" tag library, then use the "mailhide" tag.
It accepts two parameters: the first one is the e-mail address, and the optional second one is the mail subject.

Everytime a new address is used, a corresponding entry is automatically created in the database.


Example
-------

    {% load mailhide %}
    <html>
    <head>
    {% include 'inc/recaptcha.html' %}
    {% include 'inc/mailhide.html' %}
    </head>
    <body>
    {% mailhide 'test@invalid.org' %}
    {% mailhide 'test@invalid.org' 'some subject line' %}
    </body>
    </html>
