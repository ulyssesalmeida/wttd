# coding: utf-8

from django.test import TestCase
from django.db import IntegrityError
from datetime import datetime
from eventex.subscriptions.models import Subscription

class SubscriptionTest(TestCase):
	def setUp(self):
		self.obj = Subscription(
			name='Ulysses Almeida',
			cpf='12345678901',
			email='ulysses.almeida@gmail.com',
			phone='67-92391232'
			)

	def test_create(self):
		'Subscription must have name, cpf, email and phone'
		self.obj.save()
		self.assertEqual(1, self.obj.id)

	def test_has_created_at(self):
		'Subscription must have automatic created_at'
		self.obj.save()
		self.assertIsInstance(self.obj.created_at, datetime)

	def test_unicode(self):
		'Strings must be unicode'
		self.assertEqual(u'Ulysses Almeida', unicode(self.obj))

class SubscriptionUniqueTeste(TestCase):
	"""Subscriptions must be unique, let's test it"""
	def setUp(self):
		#create first entry
		Subscription.objects.create(
			name='Ulysses Almeida',
			cpf='12345678901',
			email='ulysses.almeida@gmail.com',
			phone='67-92391232'
			)

	def test_cpf_unique(self):
		'CPF must be unique'
		s = Subscription(
			name='Ulysses Almeida',
			cpf='12345678901',
			email='outro@email.com',
			phone='67-92391232'
			)
		self.assertRaises(IntegrityError, s.save)

	def test_email_unique(self):
		'Email must be unique'
		s = Subscription(
			name='Ulysses Almeida',
			cpf='10987654321',
			email='ulysses.almeida@gmail.com',
			phone='67-92391232'
			)
		self.assertRaises(IntegrityError, s.save)
