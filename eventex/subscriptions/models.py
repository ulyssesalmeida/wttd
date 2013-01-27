# coding: utf-8
from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.
class Subscription(models.Model):
	name = models.CharField(_(u'Nome'), max_length=100)
	cpf = models.CharField(_(u'CPF'), max_length=11, unique=True)
	email = models.EmailField(_(u'Email'), unique=True)
	phone = models.CharField(_(u'Telefone'), max_length=20, blank=True)
	created_at = models.DateTimeField(_(u'Criado em'), auto_now_add=True)

	class Meta:
		ordering = [u'created_at']
		verbose_name = _(u'inscrição')
		verbose_name_plural = _(u'inscrições')

	def __unicode__(self):
		return self.name