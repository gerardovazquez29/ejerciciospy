
# Calcula la tarifa del transporte público según la edad:
# - Menores de 5: gratis
# - 5-18 o mayores de 60: 50% descuento
# - Resto: tarifa completa

pasaje = int(input('ingresa tu edad: '))
tarifa_completa = 10
descuento = 0
"""
if pasaje < 5:
    print('pasaje Gratis')
elif (pasaje >= 5 and pasaje <= 18) or (pasaje >= 60):
    print('Tienes  el 50% de descuento')
else:
    print('tarifa completa')
 """
if pasaje < 5:
    descuento = 0
    print('Tu pasaje es Gratis')

elif pasaje >= 5 and pasaje <= 18:
    descuento = tarifa_completa * 0.50
    print('Tienes el 50% de Descuento')

elif pasaje >= 60:
    descuento = tarifa_completa * 0.50
    print('Tienes el 50% de Descuento')

else:
    descuento = tarifa_completa
    print('pagas tarifa completa')

print(f'pagas ${descuento:.2f}')