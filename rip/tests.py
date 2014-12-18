from django.test import TestCase
from mock_models import Service, Operation, TestCase, Condition
from testengine import Evaluate

# Create your tests here.

eval = Evaluate()

result = {}

service = Service()
service.name = "testrest"
service.host = "10.64.209.110"
service.port = "8080"

operation = Operation()
operation.name = "getTxn"
operation.url = "/orch-poc/v2/getTxn/{txnId}"
operation.method = "GET"
operation.sample_json = ''

testcase = TestCase()
testcase.id=1
testcase.name = "testCountry"
testcase.input = ''
testcase.url_kwargs = '{"txnId":"12345"}'
testcase.url_params = '{}'
testcase.exp_http_response = 200
testcase.exp_output = ''

result = eval.evaluate_testcase(service, operation, testcase)

print result
