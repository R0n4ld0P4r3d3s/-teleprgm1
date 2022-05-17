# Dado una lista de enteros, defina una función en python
# que devuelva la suma de solo los valores impares de dicha lista.

print("La suma de los números impares dada la lista de enteros de (-6,-3,-2,-1,0,5,6,9,13,14)es:")

lista = [-6,-3,-2,-1,0,5,6,9,13,14]

def sumar_impares(lista):

    if len(lista) == 0:
        return 0
    elif lista[0] % 2 == 1:
        return lista[0] + sumar_impares(lista[1:])
    else:
        return sumar_impares(lista[1:])

print(sumar_impares(lista))
