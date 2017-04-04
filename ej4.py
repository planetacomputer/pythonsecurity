#!/usr/bin/python3
import sys

def sum(number_one,number_two):
    number_one_int = convert_integer(number_one)
    number_two_int = convert_integer(number_two)
    result = number_one_int + number_two_int
    return result

def convert_integer(number_string):
    converted_integer = int(number_string)
    return converted_integer
"""
print 'Number of arguments:', len(sys.argv), 'arguments.'
print 'Argument List:', str(sys.argv)

if(len(sys.argv) != 3):
    print("El numero de args no es correcto")
else:
    answer = sum(sys.argv[1], sys.argv[2]) 
    print(answer)
"""
answer = 0
try:
    num1 = int(raw_input("Primer numero: "))
except ValueError:
    #Handle the exception
    print 'Please enter an integer. Fin de ejecucion'
    sys.exit(1)

try:
    num2 = int(raw_input("Segundo numero: "))
except ValueError:
    #Handle the exception
    print 'Please enter an integer. Fin de ejecucion'
    sys.exit(1)
else:
    answer = sum(num1, num2) 
finally:
    print("Final de programa. Esto se ejecuta siempre")

print(answer)

#c = 3/0