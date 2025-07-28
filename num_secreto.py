
import random
# Pide al usuario que adivine un número entre 1 y 10, pero solo tiene 
# 3 intentos. Si acierta, felicítalo. Si no, dile que ha perdido.

numero_secreto = random.randint(1, 10)
print('Adivina el número que tengo en mente. Solo tienes 3 intentos')

intentos = 0
max_intentos = 3
acierto = False

while intentos < max_intentos and not acierto:
    numero = int(input(f"Intento {intentos + 1}: Ingresa un número (1-10): "))
    intentos += 1
    
    if numero == numero_secreto:
        print(f"¡{numero} es correcto! ¡Felicidades!")
        acierto = True
    elif numero > numero_secreto:
        print(f"{numero} es mayor que el número secreto")
    elif numero < numero_secreto:
        print(f"{numero} es menor que el número secreto")

# Si no acertó después de todos los intentos
if not acierto:
    print("Lo siento, has perdido")
    print("Se han agotado tus intentos")
    print(f"El número secreto era: {numero_secreto}")


