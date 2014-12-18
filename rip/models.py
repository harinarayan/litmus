from django.db import models

# Create your models here.

class Service(models.Model):
	name = models.CharField(max_length=100)
	host = models.CharField(max_length=64)
	port = models.IntegerField(default=8080)

	def __unicode__(self):
		return self.name
	
class Operation(models.Model):
	service = models.ForeignKey(Service)
	name = models.CharField(max_length=100)
	url = models.CharField(max_length=255)
	METHOD_CHOICE = (
		('GET','GET'),
		('POST', 'POST'),
		('PUT', 'PUT'),
		('DELETE','DELETE'),
		('HEAD','HEAD'),
		('OPTIONS','OPTIONS'),
		('PATCH','PATCH')
	)
	method = models.CharField(max_length=7, choices=METHOD_CHOICE, default='GET')
	sample_json = models.TextField(max_length=400000)

	def __unicode__(self):
		return self.name

class TestCase(models.Model):
	operation = models.ForeignKey(Operation)
	name = models.CharField(max_length=100)
	url_kwargs = models.TextField(max_length=500, null = True)
	input = models.TextField(max_length=400000, null = True)
	url_params = models.TextField(max_length=3000, null = True)
	exp_http_response = models.IntegerField(default = 200)

	def __unicode__(self):
		return self.name
	
class Condition(models.Model):
	testcase = models.ForeignKey(TestCase)
	field = models.CharField(max_length=10000)
	OPERATOR_CHOICE = (
		('EQ', 'EQ'),
		('NE', 'NE'),
		('IN', 'IN'),
		('NI', 'NOT IN')
	)
	operator = models.CharField(max_length=19, choices=OPERATOR_CHOICE, default='EQ')
	value = models.CharField(max_length=1000)

	def __unicode__(self):
		return self.name
