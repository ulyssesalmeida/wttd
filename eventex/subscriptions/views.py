# coding: utf-8
# Create your views here.

from django.views.generic.simple import direct_to_template
from eventex.subscriptions.forms import SubscriptionForm 

def subscribe(request):
	return direct_to_template(request, 
		'subscriptions/subscription_form.html',
		{'form': SubscriptionForm()})
