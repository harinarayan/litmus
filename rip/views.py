from django.utils import timezone
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
#from django.core.urlresolvers import reverse

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView

from rip.models import Service, Operation, TestCase

from django import forms


# Service views
class ServiceListView(ListView):
	model = Service
	
	def get_context_data(self, **kwargs):
		context = super(ServiceListView, self).get_context_data(**kwargs)
		context['now'] = timezone.now()
		return context

#class ServiceForm(forms.ModelForm):
	#class Meta:
		#model = Service
		#fields = ['name', 'host', 'port']

class ServiceCreateView(CreateView):
	model = Service
	template_name_suffix = '_create_form'
	#form_class = ServiceForm
	success_url = '/rip/service'

class ServiceUpdateView(UpdateView):
	model = Service
	template_name_suffix = '_update_form'
	#form_class = ServiceForm
	success_url = '/rip/service'

def delete_service(request):
	return HttpResponse("")

def test_service(request):
	return HttpResponse("")


# Operation views
class OperationListView(ListView):
	model = Operation

	def get_queryset(self):
		queryset = Operation.objects.all().filter(service_id = self.kwargs['id'])
		return queryset
	
	def get_context_data(self, **kwargs):
		context = super(OperationListView, self).get_context_data(**kwargs)
		context['now'] = timezone.now()
		return context

class OperationDetailView(DetailView):
	model = Operation

	def get_context_data(self, **kwargs):
		context = super(OperationDetailView, self).get_context_data(**kwargs)
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
class TestCaseListView(ListView):
	model = TestCase
	
	def get_queryset(self):
		queryset = TestCase.objects.all().filter(operation_id = self.kwargs['operation_id'])
		return queryset

	def get_context_data(self, **kwargs):
		context = super(TestCaseListView, self).get_context_data(**kwargs)
		context['now'] = timezone.now()
		return context


def add_testcase(request):
	return HttpResponse("")

def edit_testcase(request):
	return HttpResponse("")

def delete_testcase(request):
	return HttpResponse("")

def test_testcase(request):
	return HttpResponse("")

