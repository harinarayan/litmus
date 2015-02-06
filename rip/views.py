import json
import difflib
import re

from django.utils import timezone
from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse_lazy, reverse

from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import login_required

from django.views.generic import View, TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from rip.models import Service, Operation, TestCase, Condition

from django import forms
from django.forms.models import inlineformset_factory

from django.template import RequestContext

from testengine import Evaluate

def home(request):
	return HttpResponseRedirect(reverse('service-list'))

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
		service = Service.objects.get(pk=self.kwargs['id'])
		context['service'] = service
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
		fields = ['name', 'url', 'method', 'sample_json', 'headers']

class OperationCreateView(CreateView):
	model = Operation
	form_class = OperationForm
	template_name_suffix = '_create_form'
	success_url = '/rip/service/%(service_id)s/operation/'
	
	def get_context_data(self, **kwargs):
		context = super(OperationCreateView, self).get_context_data(**kwargs)
		context['now'] = timezone.now()
		context['add_edit'] = "Add"
		service = Service.objects.get(pk=self.kwargs['id'])
		context['service'] = service
		return context

	def form_valid(self, form):
		# This method is called when valid form data has been POSTed.
		# It should return an HttpResponse.
		form.instance.service_id = self.kwargs['id']
		return super(OperationCreateView, self).form_valid(form)


class OperationUpdateView(UpdateView):
	model = Operation
	form_class = OperationForm
	template_name = 'rip/operation_create_form.html'
	success_url = '/rip/service/%(service_id)s/operation/'

	def get_context_data(self, **kwargs):
		context = super(OperationUpdateView, self).get_context_data(**kwargs)
		context['now'] = timezone.now()
		context['add_edit'] = "Edit"
		service = Service.objects.get(pk=self.kwargs['id'])
		context['service'] = service
		return context

	def form_valid(self, form):
		# This method is called when valid form data has been POSTed.
		# It should return an HttpResponse.
		form.instance.service_id = self.kwargs['id']
		return super(OperationUpdateView, self).form_valid(form)

class OperationDeleteView(DeleteView):
	model = Operation
	success_url = '/rip/service/%(service_id)s/operation/'

def run_operation(request, *args, **kwargs):
	response = {"status":"Passed"}

	service = Service.objects.get(pk=kwargs['id'])
	operation = Operation.objects.get(pk=kwargs['pk'])
	testcases = TestCase.objects.all().filter(operation_id=kwargs['pk'])
	
	evaluate = Evaluate()
	for tc in testcases:
		result = evaluate.evaluate_testcase(service, operation, tc)
		if result['status'] == "Failed":
			response['status'] = "Failed"
			break

	return HttpResponse(json.dumps(response), content_type="application/json")

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
		service = Service.objects.get(pk=self.kwargs['id'])
		context['service'] = service
		context['operation_id'] = self.kwargs['operation_id']
		operation = Operation.objects.get(pk=self.kwargs['operation_id'])
		context['operation'] = operation
		return context

class TestCaseForm(forms.ModelForm):
	#url_kwargs = forms.MultiValueField(fields=(forms.CharField(max_length=20), forms.CharField(max_length=20)))
	class Meta:
		model = TestCase
		fields = ['operation', 'name', 'url_kwargs', 'input', 'exp_http_response']
		labels = {
			'url_kwargs' : "URL positional parameter values",
		}

MAX_CONDITIONS = 10
ConditionFormSet = inlineformset_factory(TestCase, 
		Condition, 
		can_delete=True,
		extra=1,
		max_num=10)

def get_starter_kwargs_json(url):
	dictionary = {}
	placeholders = re.findall('\{[^{}].+?\}', url)
	for placeholder in placeholders:
		dictionary[placeholder.strip('{}')] = ""
	return json.dumps(dictionary, indent=2, separators=(',', ': '))

def submit_testcase(request, *args, **kwargs):
	condition_formset = None
	testcase = None
	operation = Operation.objects.get(pk=kwargs['operation_id'])

	if request.POST: #Create or Update case, actual operation
		form = TestCaseForm(request.POST)
		if form.is_valid():
			testcase = form.save(commit=False)

			if 'pk' in kwargs: # Update Case
				testcase.id = kwargs['pk']

			condition_formset = ConditionFormSet(request.POST, instance=testcase)
			if condition_formset.is_valid():
				testcase.save()
				condition_formset.save()                
				return HttpResponseRedirect(reverse('testcase-update', kwargs={'id':kwargs['id'], 'operation_id':kwargs['operation_id'], 'pk':testcase.id}))
		else:
			testcase = TestCase()
			condition_formset = ConditionFormSet(request.POST, instance=testcase)
	else: # Create or Update, show form 
		if 'pk' in kwargs: # Update form
			testcase = TestCase.objects.get(pk=kwargs['pk'])
			form = TestCaseForm(instance=testcase)
		else:
			form = TestCaseForm()
			form.fields['input'].initial=(operation.sample_json) #Get sample input from Operation and put it here.
			form.fields['url_kwargs'].initial=get_starter_kwargs_json(operation.url) #Put kwargs starter JSON
			testcase = TestCase()

		condition_formset = ConditionFormSet(instance=testcase)

	form.fields['operation'].initial = operation.id
	#form.fields['operation'].widget.attrs['disabled'] = True

	return render_to_response("rip/testcase_create_form.html", {
		"form": form,
		"condition_formset": condition_formset,
		"service_id":kwargs['id'],
		"operation_id":kwargs['operation_id'],
		"operation":Operation.objects.get(pk=kwargs['operation_id']),
		"testcase_id":testcase.id if testcase else None,
	}, context_instance=RequestContext(request))

def run_testcase(request, *args, **kwargs):
	service = Service.objects.get(pk=kwargs['id'])
	operation = Operation.objects.get(pk=kwargs['operation_id'])
	testcase = TestCase.objects.get(pk=kwargs['pk'])
	result = {}
	
	evaluate = Evaluate()
	try:
		result = evaluate.evaluate_testcase(service, operation, testcase)
	except Exception as e:
		result['status'] = 'Failed'
		result['reason'] = str(e)

	return HttpResponse(json.dumps(result), content_type="application/json")

class TestCaseCloneView(View):
	def get(self, request, *args, **kwargs):
		#Copy the test case object
		clone = TestCase.objects.get(pk=kwargs['pk'])
		clone.pk = None
		clone.name = clone.name + "_copy"
		clone.save()

		#Now copy all the related Condition objects.
		condition_list = Condition.objects.all().filter(testcase_id = self.kwargs['pk'])
		for c in condition_list:
			c.pk = None
			c.testcase = clone
			c.save()

		#Redirect to list of testcases.
		ka = {}
		ka['id'] = kwargs['id'] #service id
		ka['operation_id'] = kwargs['operation_id']
		return HttpResponseRedirect(reverse('testcase-list', args=[], kwargs=ka))

class TestCaseDiffView(TemplateView):
	template_name = 'rip/testcase_diff.html'
	
	def get_context_data(self, **kwargs):
		context = super(TestCaseDiffView, self).get_context_data(**kwargs)
		testcase1 = TestCase.objects.get(pk=kwargs['testcase1'])
		testcase2 = TestCase.objects.get(pk=kwargs['testcase2'])
		json1 = json.loads(testcase1.input)
		json2 = json.loads(testcase2.input)
		list_of_lines1 = (json.dumps(json1, sort_keys=True, indent=4, separators=(',', ': '))).split('\n')
		list_of_lines2 = (json.dumps(json2, sort_keys=True, indent=4, separators=(',', ': '))).split('\n')
		htmldiff = difflib.HtmlDiff()
		context['service_id'] = kwargs['id']
		context['operation_id'] = kwargs['operation_id']
		context['testcase1'] = testcase1
		context['testcase2'] = testcase2
		context['difftable'] = htmldiff.make_table(list_of_lines1, list_of_lines2, testcase1.name, testcase2.name, context=True);
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

