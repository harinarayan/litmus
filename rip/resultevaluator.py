import json, traceback 
from jsonpath_rw import jsonpath, parse

class ResultEvaluator:
	def get_json_value(self, json_object, json_expression):
		value_list = []
		ds = parse(json_expression).find(json_object)
		for d in ds:
			value_list.append(d.value)
			value_list.append(type(d.value))
		return value_list
	
	def match_json_value(self, json_object, json_expression, operator, expected_value):
		return_dict = {}
		actual_json_value = self.get_json_value(json.loads(json_object), json_expression)

		if len(actual_json_value) < 2:
			return_dict["status"] = "Failed"
			return_dict["reason"] = "Failed to retrieve value from response json based on given expression"
			return return_dict

		converted_expected_value_list = []
		converted_expected_value = ""
		try:
			if type(expected_value) == list:
				for data in expected_value:
					converted_expected_value_list.append(actual_json_value[1](data))
			else:
				converted_expected_value = actual_json_value[1](expected_value)
		except ValueError:
			return_dict["status"] = "Failed"
			return_dict["reason"] = traceback.format_exc()
			return return_dict

		if operator == "EQ":
			if converted_expected_value == actual_json_value[0]:
				return_dict["status"] = "Passed"
				return return_dict
			else:
				return_dict["status"] = "Failed"
				return_dict["reason"] = "Field => " + json_expression + " Expected value => " + converted_expected_value + " Actual value => " + actual_json_value[0]
				return return_dict
		elif operator == "NE":
			if converted_expected_value != actual_json_value[0]:
				return_dict["status"] = "Passed"
				return return_dict
			else:
				return_dict["status"] = "Failed"
				return_dict["reason"] = "Field => " + json_expression + " Expected value => " + converted_expected_value + " Actual value => " + actual_json_value[0]
				return return_dict

		elif operator == "IN":
			if converted_expected_value_list.count(actual_json_value[0]) > 0:
				return_dict["status"] = "Passed"
				return return_dict
			else:
				return_dict["status"] = "Failed"
				return_dict["reason"] = "Field => " + json_expression + " Expected value list => " + ', '.join(str(value) for value in converted_expected_value_list) + " Actual value => " + actual_json_value[0]
				return return_dict

		elif operator == "NI":
			if converted_expected_value_list.count(actual_json_value[0]) == 0:
				return_dict["status"] = "Passed"
				return return_dict
			else:
				return_dict["status"] = "Failed"
				return_dict["reason"] = "Field => " + json_expression + " Expected value list => " + ', '.join(str(value) for value in converted_expected_value_list) + " Actual value => " + actual_json_value[0]
				return return_dict
		else:
			return_dict["status"] = "Failed"
			return_dict["reason"] = traceback.format_exc()
			return return_dict

