

# Crea una calculadora que pida dos números y una operación (+, -, *, /)
# y muestre el resultado o un mensaje de error si la operación no es válida

resultado = 0
print( 'bienvenido a la calculadora simple a continuacion ingresa dos numeros')
print('1. Suma(+)')
print('2. Resta(-)')
print('3. multiplicacion(*)')
print('4. Divicion(/)')



while True:
    print(f'\n Resultado Actual {resultado}')
    operacion = input("ingresa un signo de operacion deseado (+, -, *, / ) o 's' para salir: ").lower()

    if operacion == 's':
        print('Hasta luego!')
        break
    
    if operacion not in('+','-','*','/'):
        print('operacion no valida ingreselo de nuevo')
        continue
    try:
        primer_valor = int(input('ingresa el primer numero '))
        segundo_valor = int(input('ingresa el segundo numero '))
    except ValueError:
        print('Ingresa un numero valido')
        continue

    if operacion == '+':
        resultado = primer_valor + segundo_valor
    elif operacion == '-':
        resultado = primer_valor - segundo_valor
    elif operacion == '*':
        resultado = primer_valor * segundo_valor
    elif operacion == '/':
        if segundo_valor == 0:
            print('no se puede dividir entre cero')
            continue
        resultado = primer_valor / segundo_valor
    print(f'Operacion: {primer_valor} {operacion} {segundo_valor}')
    print(f'Nuevo resultado: {resultado}')

    