.. image:: https://img.shields.io/badge/pypi-v1.0.0-blue.svg
    :target: https://github.com/tdsymonds/djangocms-flexslider
.. image:: https://img.shields.io/badge/license-MIT%20License-red.svg
    :target: https://github.com/tdsymonds/djangocms-flexslider

djangocms-typedjs
=================
This is a simple `django-cms`_ plugin that implements the `Typed.js`_ jQuery plugin.

Dependencies
------------
- django>=1.8
- django-cms>=3.2

Installation
------------
To install::

    pip install djangocms-typedjs

Then add djangocms-typedjs to your installed apps::

    INSTALLED_APPS = [
        ...
        'djangocms_typedjs',
        ...
    ]

If you're not already using `djangocms-text-ckeditor`_ then this too will need to be added to your installed apps::

    INSTALLED_APPS = [
        ...
        'djangocms_text_ckeditor',
        ...
    ]

Then run the migrations::

    ./manage.py migrate

The package assume that jQuery has been added to the site already. So if you're not using, please add to you templates/base.html:

.. code:: html

  <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js"></script>


Configuration
-------------
The Typed.js javascript by default is loaded from the below CDN. If you wish to override this, this can be done in your settings.py file by adding the below with your updated URL. This is optional. 

.. code:: python

    DJANGOCMS_TYPEDJS = {
        'JS_URL':  'https://cdnjs.cloudflare.com/ajax/libs/typed.js/1.1.4/typed.min.js',
    }

Usage
------
When creating the plugin simply name the plugin for reference purposes, specifiy if you would like to have a blinking cursor and optionally specify the JSON configuration (see `Typed.js`_ for more info). Next add a child text plugin for every sentance you would like to use. 

Djangocms-typedjs can also be used inside a text plugin. Simply add the child plugin to the text container and configure as usual, with one difference. Here child plugins cannot be added to djangocms-typedjs so the sentances need to be passed as part of the JSON config. The below code snippet demonstrates how to achieve this:

.. code:: javascript

  {
    // each of the sentances need to be set here:
    strings: ["First sentence.", "Second sentence."],
    // the stringElement needs to be set to null as I'm using this method by default.
    stringsElement: null
  }





.. _django-cms: https://github.com/divio/django-cms
.. _Typed.js: https://github.com/mattboldt/typed.js/
.. _djangocms-text-ckeditor: https://github.com/divio/djangocms-text-ckeditor
