import unittest
from app import get_cuentas, get_contactos, pagar, mostrar_historial, BD
from Cuenta import Cuenta, Lista_cuentas, Operacion
from datetime import datetime

class testCuentas(unittest.TestCase):
    def testContactos_hp(self):
        BD.vaciar()
        t_cuenta1 = Cuenta('21345', 'Arnaldo', 200, ['123', '456'])
        t_cuenta2 = Cuenta('123', 'Luisa', 400, ['456'])
        t_cuenta3 = Cuenta('456', 'Andrea', 300, ['21345'])
        BD.agregar_cuenta(t_cuenta1)
        BD.agregar_cuenta(t_cuenta2)
        BD.agregar_cuenta(t_cuenta3)
        checkservice = get_contactos('21345')
        self.assertEqual(checkservice, "123: Luisa;\n456: Andrea")

    def testContactos_donotExists(self):
        BD.vaciar()
        checkservice = get_contactos('2')
        self.assertEqual(checkservice, "No se ha encontrado la cuenta")

    def testPagar_hp(self):
        BD.vaciar()
        t_cuenta1 = Cuenta('21345', 'Arnaldo', 200, ['123', '456'])
        t_cuenta2 = Cuenta('123', 'Luisa', 400, ['456'])
        BD.agregar_cuenta(t_cuenta1)
        BD.agregar_cuenta(t_cuenta2)
        checkservice = pagar('21345', '123', 200)
        self.assertTrue(checkservice.startswith(f'Realizado en'))
    
    def testPagar_saldoInsuficiente(self):
        BD.vaciar()
        t_cuenta1 = Cuenta('21345', 'Arnaldo', 200, ['123', '456'])
        t_cuenta2 = Cuenta('123', 'Luisa', 400, ['456'])
        BD.agregar_cuenta(t_cuenta1)
        BD.agregar_cuenta(t_cuenta2)
        checkservice = pagar('21345', '123', 500)
        self.assertEqual(checkservice, "Saldo insuficiente")
    
    def testPagar_emisorNoExiste(self):
        BD.vaciar()
        t_cuenta2 = Cuenta('123', 'Luisa', 400, ['456'])
        BD.agregar_cuenta(t_cuenta2)
        checkservice = pagar('500', '123', 200)
        self.assertEqual(checkservice, "No se ha encontrado la cuenta origen")

    def testPagar_receptorNoExiste(self):
        BD.vaciar()
        t_cuenta1 = Cuenta('21345', 'Arnaldo', 200, ['123', '456'])
        BD.agregar_cuenta(t_cuenta1)
        checkservice = pagar('21345', '500', 100)
        self.assertEqual(checkservice, "No se ha encontrado la cuenta destino")
    
    def testHistorial_hp(self):
        BD.vaciar()
        t_cuenta1 = Cuenta('21345', 'Arnaldo', 200, ['123', '456'])
        t_cuenta2 = Cuenta('123', 'Luisa', 400, ['456'])
        BD.agregar_cuenta(t_cuenta1)
        BD.agregar_cuenta(t_cuenta2)
        pagar('21345', '123', 200)
        checkservice = mostrar_historial('21345')
        self.assertTrue(checkservice.startswith(f'Saldo de Arnaldo: 0;\nPago realizado de 200 a Luisa;\n'))

    def testHistorial_donotExists(self):
        BD.vaciar()
        checkservice = mostrar_historial('2')
        self.assertEqual(checkservice, "No se ha encontrado la cuenta")

if __name__ =='__main__':
    unittest.main()