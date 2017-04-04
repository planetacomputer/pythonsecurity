#!/usr/bin/python3
plainText = input ("Introduce una palabra en minusculas:")
distancia = int(input("Que distancia entre letras:"))
code = ""
for ch in plainText:
    ordValor = ord(ch)
    cipherValor=ordValor+distancia
    if cipherValor > ord('z'):
        cipherValor= ord('a') + distancia - (ord('z') - ordValor + 1)
    code+=chr(cipherValor)
print(code)