#!/usr/bin/env python
#!coding=utf-8  
import psutil
import json
import sys
def get_netcard():
    netcard_info = []
    info = psutil.net_if_addrs()
    for k,v in info.items():
        for item in v:
            if item[0] == 2 and not item[1]=='127.0.0.1':
                netcard_info.append(k)
    netcard_list = []
    netcard_dict = {"data":None}
    for interface in netcard_info:
        interface_dict = {}
        interface_dict["{#NAME}"] = interface
        netcard_list.append(interface_dict)
    netcard_dict["data"] = netcard_list
    netcard_json = json.dumps(netcard_dict, sort_keys=True, indent=4)
    return netcard_json
def get_sent():
    netcard = sys.argv[2]
    return psutil.net_io_counters(pernic=True).get(netcard).bytes_sent / 1024
def get_recv():
	netcard = sys.argv[2]
	return psutil.net_io_counters(pernic=True).get(netcard).bytes_recv / 1024
if __name__ == '__main__':
	if sys.argv[1] == "getname":
		print get_netcard()
	elif sys.argv[1] == "getsent":
		print get_sent()
	elif sys.argv[1] == "getrecv":
		print get_recv()
