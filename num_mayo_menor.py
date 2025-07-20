
#  Pide dos números y muestra cuál es mayor, menor o si son iguales.

while True:
    print('Bienvenido Ingresa dos numeros para verificar cual es el mayor o menor')
    salir = input("Presione la tecla 's' para salir o enter para continuar:  ").lower()
    if salir == 's':
        print('Hasta Luego!')
        break

    try:
        num1 = int(input('Ingresa el primer numero: '))
        num2 = int(input('Ingresa el segundo numero: '))
    except ValueError:
        print('ingresa numeros validos')
        continue

    if num1 > num2:
        print(f'{num1} es mayor')
        continue
    elif num2 == num1:
        print(f'{num2} y {num1} son iguales')
        continue
    else:
        print(f'{num2} es mayor')
        continue




