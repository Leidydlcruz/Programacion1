palabra = 'python'
lista = []

for letra in palabra:
    lista.append(letra)
print(lista)

lista = [letra for letra in palabra]
print(lista)

lista2 = [n if n * 2 > 10 else 'no' for n in range(0,21,2) ]
print(lista2)