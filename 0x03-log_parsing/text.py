#!/usr/bin/python3
import sys

zero = '68.249.9.20 - [2017-02-05 23:31:22.452556] "GET /projects/260 HTTP/1.1" 200 711 Hello\n'
one = '99.196.100.39 - [2017-02-05 23:31:22.954433] "GET /projects/260 HTTP/1.1" 401 658\n'
two = '128.230.61.246 - [2017-02-05 23:31:23.258076] "GET /projects/260 HTTP/1.1" Hello 292\n'
three = '116.82.223.35 - [2017-02-05 23:31:24.112360] "GET /projects/260 HTTP/1.1" 301 842\n'
four = 'Holberton - [2017-02-05 23:31:25.003550] "GET /projects/260 HTTP/1.1" 400 12\n'
five = '7.179.133.121 - [2017-02-05 23:31:25.003550] "GET /projects/260 HTTP/1.1" 400 12\n'
six = '188.213.11.218-[2017-02-05 23:31:21.690755] "GET /projects/260 HTTP/1.1" 401 1000\n'
seven = '128.230.61.246 - [2017-02-05 23:31:23.258076] "GET /projects/260 HTTP/1.1" 301 292\n'

arr = [zero, one, two, three, four, five, six, seven]
for i in arr:
    sys.stdout.write(i)
