#!/usr/bin/python

mi_tupla = (23, 1, 87, 12, 9, 89, 54, 43, 21, 9, 23)
x = 0
for item in mi_tupla:
    if item > 50:
        x = x + 1
        print(item)
print("Se han encontrado " + str(x) + " elementos")
lista = list(mi_tupla)
lista.sort()
print("lista ordenada:")
for item in lista:
    print(item)