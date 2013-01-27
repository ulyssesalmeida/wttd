# coding: utf-8

from django.test import TestCase
from eventex.subscriptions.models import Subscription
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


class SubscribePortTest(TestCase):
	def setUp(self):
		data = dict(
			name="Ulysses Almeida",
			cpf="12345678901",
			email="ulysses.almeida@gmail.com",
			phone="67-92321232")
		self.resp = self.client.post('/inscricao/', data)

	def test_post(self):
		'Valid POST should redirect to /inscricao/1/'
		self.assertEqual(self.resp.status_code, 302)

	def test_save(self):
		'Valid POST must be saved'
		self.assertTrue(Subscription.objects.exists())

class SubscribeInvalidPostTeste(TestCase):
	def setUp(self):
		data = dict(
			name="Ulysses Almeida",
			cpf="12345678901231",
			email="ulysses.almeida@gmail.com",
			phone="67-92321232")
		self.resp = self.client.post('/inscricao/', data)

	def test_post(self):
		'Invalid POST should not redirect'
		self.assertEqual(self.resp.status_code, 200)

	def test_form_errors(self):
		'Form must contain errors'
		self.assertTrue(self.resp.context['form'].errors)

	def test_dont_save(self):
		'Do not save data from form with errors'
		self.assertFalse(Subscription.objects.exists())
