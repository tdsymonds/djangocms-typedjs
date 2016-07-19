# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _

from cms.models import CMSPlugin


@python_2_unicode_compatible
class TypedJS(CMSPlugin):
    name = models.CharField(_('name'), max_length=50)
    blinking_cursor = models.BooleanField(_('blinking cursor'), default=True)
    json_config = models.TextField(_('JSON config'), blank=True, null=True,
        help_text=_('The JSON object passed to Typed.js. For more info <a target="_blank" href="https://github.com/mattboldt/typed.js/">click here</a>'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Typed.js')
        verbose_name_plural = _('Typed.js')
