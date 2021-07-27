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

# Ejercicios de práctica con texto
'''
Enunciado:
Realice un programa que solicite por consola 3 palabras cualesquiera
Luego el programa debe consultar al usuario como quiere ordenar las palabras
1 - Ordenar por orden alfabético (usando el operador ">")
2 - Ordenar por cantidad de letras (longitud de la palabra (len) y operador ">")

Si se ingresa "1" por consola se deben ordenar las 3 palabras por orden alfabético
e imprimir en pantalla de la mayor a la menor

Si se ingresa "2" por consola se deben ordenar las 3 palabras por cantidad de letras
e imprimir en pantalla de la mayor a la menor

IMPORTANTE: Para ordenar las palabras deben realizar condicionales compuestos o anidados,
no se busca utilizar bucles o algoritmos de ordenamiento ya que aún no hemos llegado a ese
contenido.
'''

print('Ejercicios de práctica con cadenas')
# Empezar aquí la resolución del ejercicio

palabra1 = str(input("ingrese la primer palabra: "))
palabra2 = str(input("ingrese la segunda palabra: "))
palabra3 = str(input("ingrese la tercer palabra: "))

print("pulse 1 si quiere ordenar sus palabras por orden alfabetico de mayor a menor")
print("pulse 2 si quiere ordenar sus palabras por cantidad de letras de mayor a menor")

respuesta = float(input("ingrese su respuesta a continuación: "))

if respuesta == 1: 
    if palabra1 > palabra2 and palabra2 > palabra3:
        print("el orden de sus palabras por orden alfabetico es: {} {} {}".format(palabra1, palabra2, palabra3))
    elif palabra1 > palabra3 and palabra3 > palabra2:
        print("el orden de sus palabras por orden alfabetico es: {} {} {}".format(palabra1, palabra3, palabra2))
    elif palabra2 > palabra1 and palabra1 > palabra3:
        print("el orden de sus palabras por orden alfabetico es: {} {} {}".format(palabra2, palabra1, palabra3))
    elif palabra2 > palabra3 and palabra3 > palabra1:
        print("el orden de sus palabras por orden alfabetico es: {} {} {}".format(palabra2, palabra3, palabra1))
    elif palabra3 > palabra1 and palabra1 > palabra2:
        print("el orden de sus palabras por orden alfabetico es: {} {} {}".format(palabra3, palabra1, palabra2))
    elif palabra3 > palabra2 and palabra2 > palabra1:
        print("el orden de sus palabras por orden alfabetico es: {} {} {}".format(palabra3, palabra2, palabra1))
elif respuesta == 2:
    if len(palabra1) > len(palabra2) and len(palabra2) > len(palabra3):
        print("el orden de sus palabras por cantidad de letras es: {} {} {}".format(palabra1, palabra2, palabra3))
    elif len(palabra1) > len(palabra3) and len(palabra3) > len(palabra2):
        print("el orden de sus palabras por cantidad de letras es: {} {} {}".format(palabra1, palabra3, palabra2))
    elif len(palabra2) > len(palabra1) and len(palabra1) > len(palabra3):
        print("el orden de sus palabras por cantidad de letras es: {} {} {}".format(palabra2, palabra1, palabra3))
    elif len(palabra2) >len(palabra3) and len(palabra3) > len(palabra1):
        print("el orden de sus palabras por cantidad de letras es: {} {} {}".format(palabra2, palabra3, palabra1))
    elif len(palabra3) > len(palabra1) and len(palabra1) > len(palabra2):
        print("el orden de sus palabras por cantidad de letras es: {} {} {}". format(palabra3, palabra1, palabra2))
    elif len(palabra3) > len(palabra2) and len(palabra2) > len(palabra1):
        print("el orden de sus palabras por cantidad de letras es: {} {} {}".format(palabra3, palabra2, palabra1))
else: 
    print("el numero insertado no es válido")