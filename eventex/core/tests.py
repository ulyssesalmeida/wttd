# coding: utf-8
"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from django.core.urlresolvers import reverse as r

class HomepageTest(TestCase):
	def setUp(self):
		self.resp = self.client.get(r('core:homepage'))

	def test_get(self):
		'GET / must return status code 200.'
		self.assertEqual(self.resp.status_code, 200)

	def test_template(self):
		'Homepage must use template index.html'
		self.assertTemplateUsed(self.resp, 'index.html')

# class SimpleTest(TestCase):
#     def test_basic_addition(self):
#         """
#         Tests that 1 + 1 always equals 2.
#         """
#         self.assertEqual(1 + 1, 2)
