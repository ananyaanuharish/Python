import json
import os
os.system('cls')

emp = '{"id":"07", "name":"Ananya", "Age":"21", "Department":"AIML"}'
print("This is JSON", type(emp))
print("Now converted from JSON to Python")

emp_python = json.loads(emp)
print("Converted to python", type(emp_python))
print(emp_python)