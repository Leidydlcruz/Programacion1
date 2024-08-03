texto = input("Por favor, ingresa un texto de tu preferencia: ")
texto1 = texto.lower()
print("El texto que ingresaste es:", texto1)

letra1 = input("Ingresa la primera letra: ").lower()
letra2 = input("Ingresa la segunda letra: ").lower()
letra3 = input("Ingresa la tercera letra: ").lower()
print("Las letras que ingresaste son:", letra1, letra2, letra3) 

mi_lista = ["letra1","letra2","letra3"]

conteo_letra1 = texto1.count(letra1)
conteo_letra2 = texto1.count(letra2)
conteo_letra3 = texto1.count(letra3)

print(f"La letra '{letra1}' aparece {conteo_letra1} veces.")
print(f"La letra '{letra2}' aparece {conteo_letra2} veces.")
print(f"La letra '{letra3}' aparece {conteo_letra3} veces.")

palabras = texto1.split()
numero_de_palabras = len(palabras)
print(f"El número de palabras en el texto es: {numero_de_palabras}")

primera_letra = texto1[0]
ultima_letra = texto1[-1]

print(f"La primera letra del texto es: {primera_letra}")
print(f"La última letra del texto es: {ultima_letra}")

fragmento = texto1 [::-1]
print(f"Mira el texto invertido: {fragmento}")

buscar_python = "python" in texto1
dic = {True: "La palabra 'Python' se encuentra en el texto.", False: "La palabra 'Python' no se encuentra en el texto."}
print(dic[buscar_python])