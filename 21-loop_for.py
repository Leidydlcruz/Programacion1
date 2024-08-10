# lista = ['a','b','c']

# for letra in lista:
#    print("Esta es la letra "+letra)
    
# for letra in lista:
#    numero_letra = lista.index(letra) + 1
#    print(f"Letra {numero_letra}: {letra} ")


# lista2 = ['pablo', 'juan','andrea','lucia']

# for nombre in lista2:
#    if nombre.startswith('l'):
#        print(nombre)
#    else:
#        print("Este nombre no comienza con l")
# for letra in 'python':
#    print(letra)

# for numero in[1,2,3,4]:
#    print(numero)

# for numero in (1,2,3,4,5):
#    print(numero)
    
# for a,b in [[1,2],[3,4],[5,6]]:
#    print(a)
    
dic = {'clave1':'a', 'clave2':'b'}
for item in dic:
    print(item)
    
for item in dic.values():
    print(item)

for item in dic.items():
    print(item)
    
for a, b in dic.items():
    print(a,b)