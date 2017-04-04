f = open("months.txt")
next = f.read(1)
contador = 0
while next != "":
    print(next)
    contador = contador + 1
    next = f.read(1)

print(contador)