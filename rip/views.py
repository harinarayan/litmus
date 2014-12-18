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
		context['service_id'] = self.kwargs['id']
		context['operation_id'] = self.kwargs['operation_id']
		return context

class TestCaseCreateView(CreateView):
	model = TestCase
	template_name_suffix = '_create_form'
	#success_url = '/rip/service/%(service_id)s/operation/'
	
	def get_context_data(self, **kwargs):
		context = super(TestCaseCreateView, self).get_context_data(**kwargs)
		context['now'] = timezone.now()
		context['add_edit'] = "Add"
		return context

	def get_success_url(self):
		operation = Operation.objects.get(pk = self.object.operation_id)
		service_id = operation.service_id
		success_url = '/rip/service/' + str(service_id) + '/operation/' + str(operation.id) + '/testcase'
		return success_url
	
class TestCaseUpdateView(UpdateView):
	model = TestCase
	template_name = 'rip/testcase_create_form.html'
	success_url = '/rip/service/%(service_id)s/operation/'

	def get_context_data(self, **kwargs):
		context = super(TestCaseUpdateView, self).get_context_data(**kwargs)
		context['now'] = timezone.now()
		context['add_edit'] = "Edit"
		return context

	def get_success_url(self):
		operation = Operation.objects.get(pk = self.object.operation_id)
		service_id = operation.service_id
		success_url = '/rip/service/' + str(service_id) + '/operation/' + str(operation.id) + '/testcase'
		return success_url

class TestCaseDeleteView(DeleteView):
	model = TestCase
	#success_url = '/rip/service/%(service_id)s/operation/'

	def get_success_url(self):
		operation = Operation.objects.get(pk = self.object.operation_id)
		service_id = operation.service_id
		success_url = '/rip/service/' + str(service_id) + '/operation/' + str(operation.id) + '/testcase'
		return success_url

def test_testcase(request):
	return HttpResponse("")

