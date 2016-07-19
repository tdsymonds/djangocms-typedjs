# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings


app_settings = getattr(settings, 'DJANGOCMS_TYPEDJS', {})

if 'JS_URL' not in app_settings:
    app_settings['JS_URL'] = 'https://cdnjs.cloudflare.com/ajax/libs/typed.js/1.1.4/typed.min.js'
