
# Crea un sistema que aplique descuentos basado en:
# - Monto de compra (>100: 5%, >500: 10%, >1000: 15%)
# - Si es cliente premium: +5% adicional

valor_compra_original = int(input('Ingrese el valor de la compra: '))
cliente_premium = input("ingresa un 'si' si eres cliente premium y un 'no' si no lo eres ").lower()

# Inicializar variables
valor_compra = valor_compra_original
descuento = 0
descuento_premium = 0
total = valor_compra

# Aplicar descuentos por monto
if valor_compra >= 1000:
    descuento = valor_compra * 0.15
elif valor_compra >= 500:
    descuento = valor_compra * 0.10
elif valor_compra >= 100:
    descuento = valor_compra * 0.05
else:
    descuento = 0

# Calcular total después del descuento base
total = valor_compra - descuento

# Aplicar descuento premium si corresponde
if cliente_premium == 'si':
    descuento_premium = total * 0.05
    total = total - descuento_premium

print(f'Su compra: ${valor_compra}')
print(f'Descuento base: ${descuento:.2f}')
print(f'Descuento premium: ${descuento_premium:.2f}')
print(f'Total a pagar: ${total:.2f}')



