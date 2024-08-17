# def  saludar_personas(nombre):
#     """
#     Esta funcion sirve para saludar a una persona
#     """
#     print('Hola ' + nombre)
    
# saludar_personas('Luisa')
# saludar_personas('Juan')
# saludar_personas('Jhon')


# def multiplicar(numero1, numero2):
#     return numero1*numero2

# resultado = multiplicar(5,10)
# print(resultado)

def chequear_3_cifras(lista):
    lista_3_cifras = []
    for n in lista:
        if n in range(100,1000):
            lista_3_cifras.append(n)
        else:
            pass
    return lista_3_cifras

resultado = chequear_3_cifras([580,22,1000,457])
print(resultado)
    
