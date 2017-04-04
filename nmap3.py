#!/usr/bin/python

import nmap
nm = nmap.PortScanner()
results = nm.scan('127.0.0.1', '22,25,80,448,53')
print results
for puerto in results['scan']['127.0.0.1']['tcp']['']:
	print puerto
