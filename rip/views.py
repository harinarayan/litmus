from django.utils import timezone
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from django.views.generic.list import ListView
from rip.models import Service, Operation, TestCase

# Service views
class ServiceListView(ListView):
	model = Service
	
	def get_context_data(self, **kwargs):
		context = super(ServiceListView, self).get_context_data(**kwargs)
		context['now'] = timezone.now()
		return context

def add_service(request):
	return HttpResponse("")

def edit_service(request):
	return HttpResponse("")

def delete_service(request):
	return HttpResponse("")

def test_service(request):
	return HttpResponse("")


# Operation views
class OperationListView(ListView):
	model = Operation
	
	def get_context_data(self, **kwargs):
		context = super(OperationListView, self).get_context_data(**kwargs)
		context['now'] = timezone.now()
		return context


def add_operation(request):
	return HttpResponse("")

def edit_operation(request):
	return HttpResponse("")

def delete_operation(request):
	return HttpResponse("")

def test_operation(request):
	return HttpResponse("")


# TestCase views
def list_testcases(request):
	return HttpResponse("")

def add_testcase(request):
	return HttpResponse("")

def edit_testcase(request):
	return HttpResponse("")

def delete_testcase(request):
	return HttpResponse("")

def test_testcase(request):
	return HttpResponse("")

