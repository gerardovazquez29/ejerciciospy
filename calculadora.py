def caculadora(a, b, operador):
    if operador == '+':
        return a + b
    elif operador == '-':
        return a - b
    elif operador == '*':
        return a * b
    elif operador == '/':
        return a / b
    elif operador == '%':
        return a % b
    else:
        return 'Operador inválido'
a = int(input('Digite el primer número: '))
b = int(input('Digite el segundo número: '))
operador = input('Digite el operador (+, -, *, /, %): ')
resultado = caculadora(a, b, operador)
print(f'El resultado de {a} {operador} {b} es: {resultado}')
