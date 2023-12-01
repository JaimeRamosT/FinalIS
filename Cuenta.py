class Operacion:
    def __init__(self, origen, destino, monto) -> None:
        self.origen = origen
        self.destino = destino
        self.monto = monto


class Cuenta:
    def __init__(self, id, name, saldo, contactos) -> None:
        self.id = id
        self.name = name
        self.saldo = saldo
        self.contactos = contactos
        self.historial = []

    def get_id(self):
        return self.id
    
    def get_name(self): 
        return self.name
    
    def get_saldo(self):
        return self.saldo
    
    def agregar_contacto(self, contacto):
        self.contactos.append(contacto)

    def incrementar_saldo(self, monto):
        self.saldo += monto
    
    def reducir_saldo(self, monto):
        self.saldo -= monto
    
    def anadir_historial(self, operacion):
        self.historial.append(operacion)

    def mostrar_historial(self):
        ret = ''
        ret += 'Saldo de ' + str(self.name) + ': ' + str(self.saldo) + ';\n'
        for operacion in self.historial:
            if operacion.origen == self.name:
                ret += 'Pago realizado de ' + str(operacion.monto) + ' a ' + str(operacion.destino) + ';\n'
            else:
                ret += 'Pago recibido de ' + str(operacion.monto) + ' de ' + str(operacion.origen) + ';\n'
        return ret

class Lista_cuentas:
    def __init__(self) -> None:
        self.cuentas = []
    
    def existe_cuenta(self, id:str):
        for cuenta in self.cuentas:
            if cuenta.get_id() == id:
                return True
        return False

    def agregar_cuenta(self, cuenta):
        self.cuentas.append(cuenta)
    
    def get_cuenta(self, id:str):
        for cuenta in self.cuentas:
            if cuenta.get_id() == id:
                return cuenta
        return None

    def transferir(self, id_origen, id_destino, monto):
        origen = self.get_cuenta(id_origen)
        destino = self.get_cuenta(id_destino)
        if origen != None and destino != None:
            if (origen.saldo - monto) < 0:
                return False
            origen.reducir_saldo(monto)
            destino.incrementar_saldo(monto)
            origen.anadir_historial(Operacion(origen.get_name(), destino.get_name(), monto))
            destino.anadir_historial(Operacion(origen.get_name(), destino.get_name(), monto))
            return True
        return False
    
    def mostrar_cuentas(self):
        ret = ''
        for cuenta in self.cuentas:
            ret += str(cuenta.id) + ', ' + cuenta.name + ', ' + str(cuenta.saldo) + str(cuenta.contactos) + '; '
        ret = ret[:-2]
        return ret
    
    def mostrar_contactos(self, id):
        for cuenta in self.cuentas:
            if cuenta.get_id() == id:
                res = ''
                for contacto in cuenta.contactos:
                    res += f'{contacto}: {self.get_cuenta(contacto).get_name()};\n'
                res = res[:-2]
                return res
        return None
    
    def vaciar(self):
        self.cuentas = []