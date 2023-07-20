#!/usr/bin/python3

"""
    A script that reads stdin line by line
    and computes metrics
"""

import sys
import re

count = 0
file_count = 0
status_code_count = [
    {'name': '200', 'count': 0},
    {'name': '301', 'count': 0},
    {'name': '400', 'count': 0},
    {'name': '401', 'count': 0},
    {'name': '403', 'count': 0},
    {'name': '404', 'count': 0},
    {'name': '405', 'count': 0},
    {'name': '500', 'count': 0}
]

regex = r'''\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3} - \[\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}.\d{6}\] "GET /projects/260 HTTP/1\.1" (200|301|400|401|403|404|405|500) \d{1,4}$
'''
try:
    for line in sys.stdin:
        if re.match(regex, line) is not None:
            t = re.findall("(?<!1\.1) \d{3} \d{1,4}", line)
            status_code, file_size = t[0].split()
            file_count += int(file_size)
            
            if status_code and status_code.isdigit():
                for status in status_code_count:
                    if status['name'] == status_code:
                        status['count'] += 1
        if count == 10:
            print(f'File size: {file_count}')
            for status in status_code_count:
                print(f'{status["name"]}: {status["count"]}')
            count = 0
        count += 1
except KeyboardInterrupt:
    print(f'File size: {file_count}')
    for status in status_code_count:
        print(f'{status["name"]}: {status["count"]}')
