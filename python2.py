#!/usr/bin/python

import sys


def eliminarLinea(fileName, message):
	#Abrimos archivo en solo lectura
	f = open(fileName,"r")
	# Creamos una lista con cada una de sus lineas
	lineas = f.readlines()
	# cerramos el archivo
	f.close()

	# abrimos el archivo pero vacio
	f = open(fileName,"w")

	# recorremos todas las lineas
	for linea in lineas:
		if linea != message:
			f.write(linea)
	# cerramos el archivo
	f.close()


#reemplaza la linea por el valor del parametro
eliminarLinea("/etc/squid/aulas-prohibidas.txt", "10.0.%s.0/24\n" % sys.argv[1])