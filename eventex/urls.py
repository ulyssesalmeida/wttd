from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
	url(r'^$', 'eventex.core.views.homepage', name='homepage'),
	url(r'^inscricao/$', 'eventex.subscriptions.views.subscribe', name='subscribe')
	# A complexidade que nao esta no modelo e sim no fluxo de dados
	# Nunca comece pelo modelo. Comece topdown
	# Klaus Wustefeld
	#
    # Examples:
    # url(r'^$', 'eventex.views.home', name='home'),
    # url(r'^eventex/', include('eventex.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),

    # CONTINUAR com 1:00:00

)
