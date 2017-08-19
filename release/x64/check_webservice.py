#!/usr/bin/env python
#!coding=utf-8
import suds
import sys
url = sys.argv[1]
try:
	client = suds.client.Client(url)
	print 1
except:
	print 0
