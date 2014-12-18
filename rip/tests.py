from django.test import TestCase
from mock_models import Service, Operation, TestCase, Condition
#from testengine import Evaluate

# Create your tests here.

#eval = Evaluate()

result = {}

service = Service()
service.name = "testrest"
service.host = "10.64.209.110"
service.port = "8080"

operation = Operation()
operation.name = "getTxn"
operation.url = "/orch-poc/v1/getTxn/{txnId}"
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

#result = eval.evaluate_testcase(service, operation, testcase)

print result

condition_list = []
condition = Condition()
condition.id = 1
condition.field = "transaction_request.merchant"
condition.operator = "EQ"
condition.value = "67235"
condition_list.append(condition)

condition = Condition()
condition.id = 2
condition.field = "transaction_request.merchant"
condition.operator = "NE"
condition.value = "67335"
condition_list.append(condition)

condition = Condition()
condition.id = 3
condition.field = "transaction_request.merchant"
condition.operator = "IN"
rval = [67335,673546,984763]
condition.value = rval
condition_list.append(condition)

condition = Condition()
condition.id = 4
condition.field = "transaction_request.merchant"
condition.operator = "NI"
rval = [67235,748373,89498,"alkddjd"]
condition.value = rval
condition_list.append(condition)


