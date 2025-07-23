
def modificar_entero(entero):
    entero = entero + 10
    print(f'Valor dentro de la función: {entero}')

x = 5
print(f'Valor antes de la función: {x}')
modificar_entero(x)
print(f'Valor después de la función: {x}')


def modificar_lista(lista):
    for i in range(len(lista)):
        lista[i] += 10
    print(f'Lista dentro de la función: {lista}')

mi_lista = [1, 2, 3]
print(f'Lista antes de la función: {mi_lista}')
modificar_lista(mi_lista)
print(f'Lista después de la función: {mi_lista}')
