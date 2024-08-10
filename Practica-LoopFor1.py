alumnos_clase = ['Maria', 'Angel', 'Diana', 'Carlos', 'Julieth','Gabriela', 'Leidy']

for alumno in alumnos_clase:
    print(f"Hola {alumno}")
    

lista_numeros = [1, 5, 8, 7, 6]
suma_numeros = 0

for numero in lista_numeros:
    suma_numeros = suma_numeros + numero
    suma_numeros += numero

print(f"La suma de los números es: {suma_numeros}")


lista_numeros2 = [1,5,8,7,6]

suma_pares = 0
suma_impares = 0

for numero in lista_numeros2:
    if numero % 2 == 0:
        suma_pares += numero
    else:
        suma_impares += numero

print(f"Suma de números pares: {suma_pares}")
print(f"Suma de números impares: {suma_impares}")

