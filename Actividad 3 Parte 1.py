# Defina una función en python que acepte el radio y
# devuelva el valor del área de un círculo de esas dimensiones

def calcular(r, pi):
    area = pi * r ** 2
    return (area)

from math import pi

r = float(input("Escriba el valor del radio: "))

area = pi * r ** 2

print("El área del círculo es: {}".format(area))
