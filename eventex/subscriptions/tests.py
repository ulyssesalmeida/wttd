# coding: utf-8
"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from eventex.subscriptions.forms import SubscriptionForm


class SubscribeTest(TestCase):
	def setUp(self):
		self.resp = self.client.get('/inscricao/')

	def test_get(self):
		'GET /inscricao/ must return status code 200.'
		self.assertEqual(self.resp.status_code, 200)

	def test_template(self):
		'Response should be a rendered template.'
		self.assertTemplateUsed(self.resp,
			'subscriptions/subscription_form.html')

	def test_html(self):
		'Html must contain input controls.'
		self.assertContains(self.resp, '<form')
		self.assertContains(self.resp, '<input', 6)
		self.assertContains(self.resp, 'type="text"', 4)
		self.assertContains(self.resp, "type='hidden'", 1)
		self.assertContains(self.resp, "type='submit'")

	def test_csrf(self):
		'Html must contain csrf token.'
		self.assertContains(self.resp, 'csrfmiddlewaretoken')

	def test_has_form(self):
		'Context must have subscription form.'
		form = self.resp.context['form']
		self.assertIsInstance(form, SubscriptionForm)

	def test_form_has_fields(self):
		'Form must have 4 fields.'
		form = self.resp.context['form']
		self.assertItemsEqual(['name', 'email', 'cpf', 'phone'], form.fields)


