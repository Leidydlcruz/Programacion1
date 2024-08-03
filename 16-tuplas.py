mi_tupla = (1,2,3,4)
print(type(mi_tupla))

#t = (1,"hola",3,2)

#mi_tupla2 = (1,2,(2,4),6)
#print(mi_tupla2[2][1])

mi_tupla = list(mi_tupla)
print(mi_tupla)
print(type(mi_tupla))

t = (1,2,3)
x,y,z = t
print(x,y,z)

longitud = len(t)
print(longitud)


t = (1,2,3,7,1)
x,y,z,u,g = t
print(x,y,z)
print(len(t))
print(t.count(1))
