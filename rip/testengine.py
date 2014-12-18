from models import Service, Operation, TestCase, Condition
import json
import httplib
from resultevaluator import ResultEvaluator

class Evaluate:
	
	def __init__(self):
		self.service=""
		self.operation=""
		self.testcase=""

	def evaluate_testcase(self, service, operation, testcase):
		eval_result_list={}
		host = service.host
		port = service.port
		operation_method = operation.method
		operation_url = self.get_complete_url(operation, testcase)
		
		server_output = self.get_server_output(host, port, operation_url, operation_method, testcase.input)

		if server_output["status"] != testcase.exp_http_response:
			eval_result_list["status"] = "Failed"
			eval_result_list["reason"] = "HTTP response mismatch. Status => " + str(server_output["status"]) + " Reason => " + server_output["reason"]
			return eval_result_list

		testcase_id = testcase.id
		condition_list = self.get_eval_conditions(testcase_id)

		if len(condition_list) > 0:
			try:
				json_data = json.loads(server_output["json_data"])
			except ValueError:
				eval_result_list["status"] = "Failed"
				eval_result_list["reason"] = "There are conditions defined on JSON data received from server but Output from server is not a valid JSON data"
				return eval_result_list

		conditions_eval_result = {}
		for condition in condition_list:
			result_evaluator = ResultEvaluator()
			eval_result = result_evaluator.match_json_value(server_output["json_data"], condition.field, condition.operator, condition.value)
			conditions_eval_result[condition.id] = eval_result

		status = "Passed"
		for condition_id, result in conditions_eval_result.items():
			if "Passed" != result["status"]:
				status = "Failed"
				break
		
		if "Passed" == status:
			eval_result_list["status"] = "Passed"
		else:
			eval_result_list["status"] = "Failed"
			eval_result_list["reason"] = "One or More Condition evaluation Failed"

		eval_result_list["conditions"] = conditions_eval_result
		return eval_result_list
	
	def get_server_output(self, host, port, url, method, input):
		server_response = {}
		conn = httplib.HTTPConnection(host, port)
		headers = {"Content-Type":"application/json"}
		conn.request(method, url, input, headers)
		res = conn.getresponse()
		server_response["status"] = res.status
		server_response["reason"] = res.reason
		server_response["json_data"] = res.read()
		
		return server_response
		
	
	def get_complete_url(self, operation, testcase):
		opetation_url = operation.url

		tc_url_kwargs = testcase.url_kwargs
		tc_url_params = testcase.url_params
		tc_url_params = '{}'
		tc_url_kwargs_json = json.loads(tc_url_kwargs)
		tc_url_params_json = json.loads(tc_url_params)
		tc_url_kwargs_dict = json.dumps(tc_url_kwargs_json)
		tc_url_params_dict = json.dumps(tc_url_params_json)

		if len(tc_url_kwargs_dict) > 0:
			for tc_url_key,tc_url_val in tc_url_kwargs_json.items():
				replace_str = "{" + tc_url_key + "}"
				opetation_url = opetation_url.replace(replace_str, tc_url_val)

		if len(tc_url_params_dict) > 0:
			opetation_url = opetation_url + "?"
			for tc_url_key, tc_url_val in tc_url_params_json.items():
				opetation_url = opetation_url + tc_url_key + "=" + tc_url_val + "&"	
			opetation_url = opetation_url[:-1]

		return opetation_url


	def get_eval_conditions(self, testcase_id):
		
		condition_list = Condition.objects.all().filter(testcase=testcase_id)	
		return condition_list
