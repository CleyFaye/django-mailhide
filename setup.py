#!/usr/bin/env python3
import os
from setuptools import setup


def read(fname,
         ):
    """Utility function to read the README file.

    Notes
    -----
    This is used for the long_description.
    """
    return open(os.path.join(os.path.dirname(__file__),
                             fname),
                'r').read()


setup(name="django-mailhide",
      version="1.0.0",
      author="Gabriel Paul 'Cley Faye' Risterucci",
      author_email="gabriel.risterucci@gmail.com",
      description=("Provide template tags to protect e-mail in a Django "
                   "application using reCAPTCHA"),
      license="MIT",
      keywords="django templatetags email recaptcha",
      url="https://repos.cleyfaye.net/trac/django-mailhide",
      packages=['mailhide',
                'mailhide.api',
                'mailhide.migrations',
                'mailhide.models',
                'mailhide.templatetags'],
      include_package_data=True,
      install_requires=['pycaptcha'],
      long_description=read('README.md'),
      python_requires='>=3',
      classifiers=[
          "Development Status :: 4 - Beta",
          "Topic :: Internet :: WWW/HTTP :: Dynamic Content :: "
          + "CGI Tools/Libraries",
          "Framework :: Django :: 1.11",
          "License :: OSI Approved :: MIT License",
      ],
      )
