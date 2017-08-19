#!/usr/bin/env python
#!coding=utf-8
import socket
import sys
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host = sys.argv[1]
port = int(sys.argv[2])
time = int(sys.argv[3])
s.settimeout(time)
try:
    s.connect((host, port))
    print(1)
except socket.timeout:
    print(0)
except Exception as err:
    print(2)
