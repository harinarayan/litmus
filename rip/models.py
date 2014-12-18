from django.db import models

# Create your models here.

class Service(models.Model):
	name = models.CharField(max_length=100)
	host = models.CharField(max_length=64)
	port = models.IntegerField(default=8080)
	
class Operation(models.Model):
	service = models.ForeignKey(Service)
	name = models.CharField(max_length=100)
	url = models.CharField(max_length=255)
	sample_json = models.CharField(max_length=400000)

class TestCase(models.Model):
	operation = models.ForeignKey(Operation)
	name = models.CharField(max_length=100)
	input = models.CharField(max_length=400000)
	exp_http_response = models.IntegerField(default = 200)
	exp_output = models.CharField(max_length=400000)
	
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
