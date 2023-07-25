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
sc = [
        '200', '301', '400', '401',
        '403', '404', '405', '500'
]

try:
    for line in sys.stdin:
        t = line.split()
        if count == 10:
            print(f'File size: {file_count}')
            for status in status_code_count:
                if status['count'] != 0:
                    print(f'{status["name"]}: {status["count"]}')
            count = 0

        status_code, file_size = None, None
        if len(t) >= 1:
            for i in range(len(t)):
                if t[i] in sc and t[i - 1] not in sc:
                    status_code = t[i]
                elif t[i].isdigit():
                    file_size = int(t[i])
        if file_size:
            file_count += file_size
        if status_code and status_code.isdigit():
            for status in status_code_count:
                if status['name'] == status_code:
                    status['count'] += 1
        count += 1
except KeyboardInterrupt:
    pass

print(f'File size: {file_count}')
for status in status_code_count:
    if status['count'] != 0:
        print(f'{status["name"]}: {status["count"]}')
