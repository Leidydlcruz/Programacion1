class Cuenta:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo
    
    def retirar(self, monto_retiro):
        if self.saldo >= monto_retiro:
            self.saldo -= monto_retiro
            print("Retiro realizado")
        else:
            print("Fondos insuficientes")
    
    def __str__(self):
        return f"Titular: {self.titular}, Saldo: {self.saldo}"

class Banco:
    def __init__(self):
        self.cuentas = []
    
    def agregar_cuenta(self, cuenta):
        self.cuentas.append(cuenta)
        print(f"Cuenta de {cuenta.titular} agregada.")
    
    def eliminar_cuenta(self, nombre_cuenta):
        for cuenta in self.cuentas:
            if cuenta.titular == nombre_cuenta:
                self.cuentas.remove(cuenta)
                print(f"Cuenta de {nombre_cuenta} eliminada.")
                return

    def mostrar_cuentas(self):
        for cuenta in self.cuentas:
            print(cuenta)

cuenta1 = Cuenta("Leidy", 500000)
cuenta2 = Cuenta("Maria", 1000000)

banco = Banco()
banco.agregar_cuenta(cuenta1)
banco.agregar_cuenta(cuenta2)
banco.mostrar_cuentas()

cuenta1.retirar(200000)
banco.eliminar_cuenta("Maria")
banco.mostrar_cuentas()
