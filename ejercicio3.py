lista = [item for item in range(11)]

def es_multiplo(x):
    return x % 3 == 0
lista2 = list(filter(es_multiplo, lista))
print(lista2)


# Alternativa usando lambda
lista3 = list(filter(lambda x: x % 3 == 0, lista))
print(lista3)