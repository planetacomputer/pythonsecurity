#!/usr/bin/python3
code = input("Texto encriptado:")
distancia = int(input("Distancia: "))
plainText=''
for ch in code:
    ordValue = ord(ch)
    cipherValue = ordValue - distancia
    if cipherValue < ord('a'):
        cipherValue=ord('z')-(distancia-(ord('a')-ordValue+1))
    plainText += chr(cipherValue)
print(plainText)