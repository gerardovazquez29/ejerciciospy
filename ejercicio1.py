
def calcular_maximo(n1,n2,n3):
   
    if n1 >= n2 and n1 >= n3:
        mayor = n1
    elif n2 >= n1 and n2 >= n3:
        mayor = n2
    else:
        mayor = n3
    return mayor
n1= int(input("Ingrese el primer número: "))
n2= int(input("Ingrese el segundo número: "))   
n3= int(input("Ingrese el tercer número: "))
maximo = calcular_maximo(n1, n2, n3)
print(f"El número mayor es: {maximo}")


def operaciones(*numeros):
    suma = 0
    resta = 0
    multiplicacion = 1
    division = 1
    for numero in numeros:
        suma += numero
        resta -= numero
        multiplicacion *= numero
        if numero != 0:
            division /= numero

    return suma, resta, multiplicacion, division
sum,rest,mult,div = operaciones(5,3,2,9,10)
print(f"Suma: {sum}")
print(f"Resta: {rest}")
print(f"Multiplicación: {mult}")
print(f"División: {div}")
