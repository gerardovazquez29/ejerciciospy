"""
nota = 80

if nota >= 90:
    print('aprobaste la materia')
    print('felicidades exelente calificacion')
elif nota >= 80:
    print('aprobaste la materia')
    print('felicidades Buenas calificaciones')
elif nota >= 60:
    print('aprobaste la materia')
else:
    print('Reprobaste la materia')
"""

frutas_favoritas = ['manzana', 'platano','mango', 'zandia']

fruta = input('Ingresa tu fruta Favorita: ')

if fruta in frutas_favoritas:
    print(f'{fruta} es una fruta delisiosa')
else:
    print(f'{fruta} no es una fruta delisiosa')
