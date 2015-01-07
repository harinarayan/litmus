
class Service:
	name = "testrest"
	host = "10.64.209.110"
	port = "8080"
	protocol = "HTTP"

class Operation:
	name = "getTxn"
	url = "/orch-poc/v1/getTxn/{txnId}"
	method = "GET"
	sample_json = ''
	headers = '{"Content-Type":"application/json"}'

class TestCase:
	name = "testCountry"
	input = ''
	url_kwargs = {"txnId":"12345"}
	url_params = {}
	exp_http_response = 200
	exp_output = ''

class Condition:
	field = ''
	operator = "EQ"
	value = "US"

