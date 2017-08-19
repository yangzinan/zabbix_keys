#!/usr/bin/env python
#!coding=utf8
import psutil
import sys
import json

def get_devices():
	disks = psutil.disk_partitions()
	disk_dict = {"data":None}
	disk_list = []
	driver_list = []
	i = 1
	j = 1
	for disk in disks:
		if disk.mountpoint != '/' and disk.mountpoint != "/dev/shm" and disk.mountpoint != "/boot":
			driver = disk.device
			driver = driver.split("/")[2]
			if driver == 'mapper':
				if j == 1:
					driver = 'dm-' + str(i)
				else:
					driver = 'dm-' + str(i + 1)
				i = i + 1
			test_list = []
			test_list.append(driver)
			test_list.append(disk.mountpoint)
			driver_list.append(test_list)
		j = j + 1
	for driver in driver_list:
		dirver_dict = {}
		dirver_dict["{#NAME}"] = driver[0]
		dirver_dict["{#MOUNT}"] = driver[1]
		disk_list.append(dirver_dict)
	disk_dict["data"] = disk_list
	disks_json = json.dumps(disk_dict, sort_keys=True, indent=4)
	return disks_json
def get_root():
	disks = psutil.disk_partitions()
	root_dict = {"data":None}
	i = 0
	for disk in disks:
		if 'mapper' in disk.device:
			i = i + 1
		if disk.mountpoint == "/":
			root = disk.device
			root = root.split("/")[2]
			if root == 'mapper':
				root = 'dm-' + str(i)
	root_dict1 = {}
	root_list = []
	root_dict1["{#NAME}"] = root
	root_list.append(root_dict1)
	root_dict["data"] = root_list
	root_json = json.dumps(root_dict, sort_keys=True, indent=4)
	return root_json
def get_sent():
	info = psutil.disk_io_counters(perdisk=True)
	return (info[sys.argv[2]].read_bytes / 1024)
def get_recv():
	info = psutil.disk_io_counters(perdisk=True)
	return (info[sys.argv[2]]. write_bytes / 1024)

if __name__ == '__main__':
	disks = psutil.disk_partitions()
	if sys.argv[1] == "getdevices":
		print get_devices()
	elif sys.argv[1] == 'getsent':
		print get_sent()
	elif sys.argv[1] == 'getrecv':
		print get_recv()
	elif sys.argv[1] == 'getroot':
		print get_root()


