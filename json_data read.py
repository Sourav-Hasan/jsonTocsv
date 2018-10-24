import json

import csv

input_file = open('a.json')
json_str = input_file.read()

employee_parsed = json.loads(json_str)

emp_data = employee_parsed['employees']

# open a file for writing

employ_data = open('EmployData.csv', 'w')

# create the csv writer object

csvwriter = csv.writer(employ_data)

count = 0

for emp in emp_data:

      if count == 0:

             header = emp.keys()

             csvwriter.writerow(header)

             count += 1

      csvwriter.writerow(emp.values())

employ_data.close()
