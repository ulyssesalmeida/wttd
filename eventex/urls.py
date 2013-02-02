# coding: utf-8
from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
	# A complexidade que nao esta no modelo e sim no fluxo de dados
	# Nunca comece pelo modelo. Comece topdown
	# Klaus Wustefeld

    #reverse é algo legal.  from django.core.urlresolvers import reverse

	#
    # Examples:
    # url(r'^$', 'eventex.views.home', name='home'),
    # url(r'^eventex/', include('eventex.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    url(r'^inscricao/', include('eventex.subscriptions.urls', namespace='subscriptions')),
    url(r'^', include('eventex.core.urls', namespace='core')),
)
