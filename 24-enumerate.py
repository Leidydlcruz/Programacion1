lista = ['a','b','c']

for item in enumerate(lista):
     print(item)

for indice, elemento in enumerate(range(50,55)):
    print(indice, elemento)
    
mis_tuplas = list(enumerate(lista))
print(mis_tuplas)


lista_indices = list(enumerate("Python"))
print(lista_indices)

palabra = "Python"
lista_indices = list(enumerate(palabra))
print(lista_indices)

lista_nombres = ['Marcos','Laura','Monica','Javier']

for i, nombre in enumerate(lista_nombres):
    if nombre[0] == 'M':
        print(i)