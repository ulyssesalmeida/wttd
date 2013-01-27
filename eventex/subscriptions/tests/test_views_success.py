# coding: utf-8

from django.test import TestCase
from eventex.subscriptions.models import Subscription


class SuccessTest(TestCase):
	def setUp(self):
		s = Subscription.objects.create(
			name='Ulysses Almeida', 
			cpf='12345678901',
			email='ulysses.almeida@gmail.com',
			phone='67-81112764'
			)
		self.resp = self.client.get('/inscricao/%d/' % s.pk)

	def test_get(self):
		'GET /inscricao/1/ should return status 200'
		self.assertEqual(self.resp.status_code, 200)

	def test_template(self):
		'Uses template'
		self.assertTemplateUsed(self.resp, 'subscriptions/subscription_detail.html')

	def test_context(self):
		'Context must have a subsbcription instance.'
		subsbcription = self.resp.context['subscription']
		self.assertIsInstance(subsbcription, Subscription)

	def test_html(self):
		'Check if subscriptio data was renderes.'
		self.assertContains(self.resp, 'Ulysses Almeida')

class SuccessNotFound(TestCase):
	def test_not_found(self):
		resp = self.client.get('/inscricao/0/')
		self.assertEqual(resp.status_code, 404)
		