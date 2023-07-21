#!/usr/bin/python3
import sys

first = "253.56.23.89 - [2023-12-03 09:34:23.354526] \"GET /projects/260 HTTP/1.1\" 200 456\n"
second = "253.56.23.89 - [2023-12-03 09:34:23.354526] \"GET /projects/260 HTTP/1.1\"  400 456\n"
third = "253.56.23.89 - [2023-12-03 09:34:23.354526] \"GET /projects/260 HTTP/1.1\" 500 456\n"

arr = [first, second, third]

for i in arr:
    sys.stdout.write(i)
