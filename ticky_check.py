#!/usr/bin/python3

import re
import csv
import operator
import os

errors = {}
users = {}

error_pattern = r'ticky: ERROR ([\w\' ]*) \((.+)\)'
info_pattern = r'ticky: INFO ([\w\' ]*) \[#(\d+)\] \((.+)\)'

logfile = os.path.expanduser('~') + '/data/syslog.log'

with open(logfile) as f:
  lines = f.readlines()
  for line in lines:
    result_error = re.search(error_pattern, line)
    result_info = re.search(info_pattern, line)
    if result_error:
      errors.setdefault(result_error[1], 0)
      errors[result_error[1]] += 1
      users.setdefault(result_error[2],[0,0])
      users[result_error[2]][1] += 1
    if result_info:
      users.setdefault(result_info[3],[0,0])
      users[result_info[3]][0] += 1

error_count = sorted(errors.items(), key = operator.itemgetter(1), reverse = True)
user_stats = sorted(users.items())

print(error_count)
print(user_stats)

output_error = os.path.expanduser('~') + '/data/error_message.csv'
output_user = os.path.expanduser('~') + '/data/user_statistics.csv'
 
with open(output_error, 'w') as f:
  writer = csv.writer(f)
  writer.writerow(['Error', 'Count'])
  writer.writerows(error_count)

with open(output_user, 'w') as f:
  writer = csv.writer(f)
  writer.writerow(['Username', 'INFO', 'ERROR'])
  for item in user_stats:
    writer.writerow([item[0], item[1][0], item[1][1]])
