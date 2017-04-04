palabra = raw_input("Introduce la palabra: ")
posiciones = raw_input("Introduce el numero de posiciones: ")

for c in palabra:
    codNum = ord(c)
    codNum2 = codNum + int(posiciones)
    print codNum2
    
    