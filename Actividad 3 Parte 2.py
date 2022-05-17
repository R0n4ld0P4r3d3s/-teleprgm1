# Defina una función en python que acepte 3 valores
# y devuelva solo el máximo de los tres.


def numero_mayor(n1, n2, n3):
    if n1 > n2 and n1 > n3:
        return n1
    elif n2 > n1 and n2 > n3:
        return n2
    elif n3 > n1 and n3 > n2:
        return n3
    elif n1 == n2 > n3:
        return n1
    elif n1 == n3 > n2:
        return n1
    elif n2 == n3 > n1:
        return n2
    else:
        return n1

n1 = float(input("Ingrese un número: "))
n2 = float(input("Ingrese un número: "))
n3 = float(input("Ingrese un número: "))

resultado = numero_mayor(n1, n2, n3)
print ("El número mayor es: ", resultado)
