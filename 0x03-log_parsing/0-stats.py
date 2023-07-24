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
status_codes = [
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
        status_code, file_size = 0, 0
        if len(t) >= 2:
            for i in range(len(t)):
                if t[i] in status_codes:
                    status_code = t[i]
                    if i + 1 < len(t):
                        if t[i + 1].isdigit():
                            file_size = t[i + 1]
                elif t[i].isdigit():
                    file_size = t[i]

        file_count += int(file_size)

        if status_code in status_codes:
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
