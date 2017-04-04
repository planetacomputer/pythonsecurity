#!/usr/bin/python

import time
# En primer lugar debemos de abrir el fichero que vamos a leer.
# Usa 'rb' en vez de 'r' si se trata de un fichero binario.
fechaActualizacion = 'Escaneo efectuado el ' + time.strftime('%d %b %y')
infile = open(time.strftime('%y%m%d-%H:%M:%S')+'texto.txt', 'w')
# Mostramos por pantalla lo que leemos desde el fichero
print('>>> Escritura completa del fichero')
print(infile.write("holA"))
# Cerramos el fichero.
infile.close()