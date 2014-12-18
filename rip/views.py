from django.utils import timezone
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse_lazy

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

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

class ServiceDeleteView(DeleteView):
	model = Service
	success_url = reverse_lazy('service-list')

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
		context['service_id'] = self.kwargs['id']
		return context

class OperationDetailView(DetailView):
	model = Operation

	def get_context_data(self, **kwargs):
		context = super(OperationDetailView, self).get_context_data(**kwargs)
		context['now'] = timezone.now()
		return context

class OperationForm(forms.ModelForm):
	class Meta:
		model = Operation
		fields = ['name', 'url', 'method', 'sample_json']

class OperationCreateView(CreateView):
	model = Operation
	template_name_suffix = '_create_form'
	success_url = '/rip/service/%(service_id)s/operation/'
	
	def get_context_data(self, **kwargs):
		context = super(OperationCreateView, self).get_context_data(**kwargs)
		context['now'] = timezone.now()
		context['add_edit'] = "Add"
		return context

class OperationUpdateView(UpdateView):
	model = Operation
	template_name = 'rip/operation_create_form.html'
	success_url = '/rip/service/%(service_id)s/operation/'

	def get_context_data(self, **kwargs):
		context = super(OperationUpdateView, self).get_context_data(**kwargs)
		context['now'] = timezone.now()
		context['add_edit'] = "Edit"
		return context

class OperationDeleteView(DeleteView):
	model = Operation
	success_url = '/rip/service/%(service_id)s/operation/'

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

