nombre = input("Ingresar nombre: ")
ventas = float(input("¿Cuánto has vendido este mes?: "))
porcentaje = (13/100)

comisiones = round((ventas * porcentaje), 2 )

print(f"¡Hola! {nombre}, segun tus ventas de {ventas} tus comisiones son {comisiones}")