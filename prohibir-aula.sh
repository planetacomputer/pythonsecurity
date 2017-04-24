#/bin/bash
# 
# Script para prohibir la navegación de un aula
# Se creará el rango del aula en /etc/squid/aulas-prohibidas.txt
# Indicar el número de aula al ejecutar el script

echo "Hola"
if [ $# -ne 1 ]; then
	echo "Es necesario introducir el numero de aula a prohibir"
	exit -1
fi
echo Prohibir navegar aula $1, subred 10.0.$1.0/24
echo 10.0.$1.0/24 >> /etc/squid/aulas-prohibidas.txt

service squid reload
echo subredes denegadas:
cat /etc/squid/aulas-prohibidas.txt