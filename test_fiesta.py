# Pruebas para verificar la lógica de la fiesta

print("=== Casos de prueba ===")

# Caso 1: Mayor de edad
print("\nCaso 1: Persona mayor de edad")
persona = 20
acompañado_adulto = False
if persona >= 18:
    print('Puede entrar ala fiesta sin restricciones')
elif persona < 18 and acompañado_adulto:
    print('Puede entrar con adulto pero no puede consumir alcohol')
else:
    print('No puede entrar ala fiesta')

# Caso 2: Menor con adulto
print("\nCaso 2: Menor con adulto")
persona = 16
acompañado_adulto = True
if persona >= 18:
    print('Puede entrar ala fiesta sin restricciones')
elif persona < 18 and acompañado_adulto:
    print('Puede entrar con adulto pero no puede consumir alcohol')
else:
    print('No puede entrar ala fiesta')

# Caso 3: Menor sin adulto
print("\nCaso 3: Menor sin adulto")
persona = 15
acompañado_adulto = False
if persona >= 18:
    print('Puede entrar ala fiesta sin restricciones')
elif persona < 18 and acompañado_adulto:
    print('Puede entrar con adulto pero no puede consumir alcohol')
else:
    print('No puede entrar ala fiesta')
