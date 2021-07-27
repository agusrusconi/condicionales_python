# Condicionales [Python]
# Ejercicios de profundización

# Autor: Inove Coding School
# Version: 2.0

# NOTA: 
# Estos ejercicios son de mayor dificultad que los de clase y práctica.
# Están pensados para aquellos con conocimientos previo o que dispongan
# de mucho más tiempo para abordar estos temas por su cuenta.
# Requiere mayor tiempo de dedicación e investigación autodidacta.

# IMPORTANTE: NO borrar los comentarios en VERDE o NARANJA

# Ejercicios de práctica con números
'''
Enunciado:
Realice un programa que solicite por consola 2 números
Calcule la diferencia entre ellos e informe por pantalla
si el resultado es positivo, negativo o cero.
'''

print('Ejercicios de práctica con números')
# Empezar aquí la resolución del ejercicio

numero1 = int(input("ingrese el primer numero: "))
numero2 = int(input("ingrese el segundo numero: "))

resultado1 = numero1 - numero2
resultado2 = numero2 - numero1

if numero1 > numero2:
    print("la diferencia entre los numeros ingresados es: {}".format(resultado1))
elif numero2 > numero1:
    print("la diferencia entre los numeros ingresados es: {}".format(resultado2))
else:
    print("los numeros ingresados tienen el mismo valor")
    
if resultado1 > 0 or resultado2 > 0:
    print("el resultado es positivo")
elif resultado1 < 0 or resultado2 < 0:
    print("el resultado es negativo")
else:
    print("el resultado es 0")
