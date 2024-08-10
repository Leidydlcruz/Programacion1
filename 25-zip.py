nombres = ['Ana', 'Pedro', 'Lorena']
edades = [20,50,15,20,40]

combinados = list(zip(nombres, edades))
print(combinados)

for nombre, edad in combinados:
    print(f"{nombre} tiene {edad}")