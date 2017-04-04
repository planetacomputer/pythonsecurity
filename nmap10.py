#!/usr/bin/python

import nmap
import time

nm = nmap.PortScanner()

# Pide el rango del escaneo mientras este sea nulo
#host_scan = raw_input('Host scan: ')
#while host_scan == "":
#    host_scan = raw_input('Host scan: ')

nm.scan('127.0.0.1', '22-443')
#nm.scan(host_scan, '22-443')

print nm.command_line()
###print nm.scaninfo()
###nm.all_hosts()
###nm['127.0.0.1'].hostname()
###nm['127.0.0.1'].state()
###nm['127.0.0.1'].all_protocols()
###nm['127.0.0.1']['tcp'].keys()
###nm['127.0.0.1'].has_tcp(22)
###nm['127.0.0.1'].has_tcp(23)
###nm['127.0.0.1']['tcp'][22]
###nm['127.0.0.1'].tcp(22)
###print nm['127.0.0.1']['tcp'][22]['state']

hosts_list = [(x, nm[x]['status']['state']) for x in nm.all_hosts()]
print hosts_list

for host in nm.all_hosts():
     print('----------------------------------------------------')
     print('Host : %s (%s)' % (host, nm[host].hostname()))
     print('State : %s' % nm[host].state())
     for proto in nm[host].all_protocols():
         print('----------')
         print('Protocol : %s' % proto)
 
         lport = nm[host][proto].keys()
         lport.sort()
         for port in lport:
             print ('port : %s\tstate : %s' % (port, nm[host][proto][port]['state']))


#Mostrar la fecha en formato DIA/MES/ANYO y HORA/MINUTOS/SEGUNDOS
fechaActualizacion = 'Escaneo efectuado el ' + time.strftime('%d %b %y') + ' a las ' + time.strftime('%H:%M:%S')  + '\n'
nombre_fichero = "/home/ubuntu/Python/" + "Scan" + time.strftime("%y"+"%m"+"%d") + time.strftime("%H"+"%M"+"%S")
print nombre_fichero


archivo = open(nombre_fichero, 'w+')
archivo.write(fechaActualizacion)
hostsActivos = 0
hostsTotales = 0
for host, status in hosts_list:
    if status == 'up':
        hostsActivos += 1
        print host, status
        archivo.write(host + '\n')
    hostsTotales += 1
archivo.write('Se han encontrado ' + str(hostsActivos) + ' hosts activos de un total de ' + str(hostsTotales) + ' escaneados\n')
archivo.write('----------------------\n')
archivo.close()

###print(nm.csv())