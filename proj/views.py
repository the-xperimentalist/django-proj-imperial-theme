from django.shortcuts import render, get_object_or_404
from django.http import Http404, HttpResponse
from django.template import loader
from .models import Portfolio, Service

def index(request):
	all_services = Service.objects.all()
	all_portfolio = Portfolio.objects.all()
	context = {
		'all_portfolio' : all_portfolio,
		'all_services' : all_services,
	}
	return render(request, 'proj/index.html', context)



