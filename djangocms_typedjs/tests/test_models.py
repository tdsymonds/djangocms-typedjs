# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.files import File

from cms.test_utils.testcases import CMSTestCase

from ..models import TypedJS


class TypedJSTest(CMSTestCase):
    def test_creating_new_slider(self):
        t = TypedJS.objects.create(name='test')

        all_typedjs = TypedJS.objects.all()

        self.assertEqual(all_typedjs.count(), 1)
        self.assertEqual(all_typedjs[0], t)
        self.assertEqual(t.__str__(), t.name)
