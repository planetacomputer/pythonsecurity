#!/usr/bin/python

import nmap
nm = nmap.PortScanner()
host_scan = raw_input('Host scan: ')
while host_scan == "":
    host_scan = raw_input('Host scan: ')
nm.scan(hosts=host_scan, arguments='-n -sP -PE -PA21,23,80,3389')
print nm.all_hosts()