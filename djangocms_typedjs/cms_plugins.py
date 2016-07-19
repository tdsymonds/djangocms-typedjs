# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.utils.translation import ugettext_lazy as _

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from .models import TypedJS
from .settings import app_settings


class TypedJSPlugin(CMSPluginBase):
    name = _('Typed.js')
    module = _('Typed.js')
    model = TypedJS
    render_template = 'djangocms_typedjs/_typedjs.html'
    cache = False
    allow_children = True
    child_classes = ['TextPlugin', ]
    text_enabled = True

    def render(self, context, instance, placeholder):
        context = super(TypedJSPlugin, self).render(context, instance, placeholder)
        context['app_settings'] = app_settings
        return context

    def icon_src(self, instance):
        return settings.STATIC_URL + 'djangocms_typedjs/images/djangocms-typedjs-icon.png'

    def icon_alt(self, instance):
        return u'Django CMS Typed.js plugin: %s' % instance.name

plugin_pool.register_plugin(TypedJSPlugin)
