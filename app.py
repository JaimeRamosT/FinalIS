from flask import Flask, jsonify, request
from Cuenta import Cuenta, Lista_cuentas, Operacion
from datetime import datetime

app = Flask(__name__)

BD = Lista_cuentas()

@app.route('/', methods=['GET'])
def init_app():
    t_cuenta1 = Cuenta('21345', 'Arnaldo', 200, ['123', '456'])
    t_cuenta2 = Cuenta('123', 'Luisa', 400, ['456'])
    t_cuenta3 = Cuenta('456', 'Andrea', 300, ['21345'])
    BD.agregar_cuenta(t_cuenta1)
    BD.agregar_cuenta(t_cuenta2)
    BD.agregar_cuenta(t_cuenta3)

    return jsonify({
        'success': True,
        'cuentas': BD.mostrar_cuentas()
    })

@app.route('/billetera/cuentas', methods=['GET'])
def get_cuentas():
    acc = BD.mostrar_cuentas()
    return jsonify({
        'success': True,
        'cuentas': acc
    })

@app.route('/billetera/contactos/<minumero>', methods=['GET'])
def get_contactos(minumero):
    if(not BD.existe_cuenta(str(minumero))):
        return 'No se ha encontrado la cuenta'
    else:
        contactos = BD.mostrar_contactos(str(minumero))
        return contactos

@app.route('/billetera/pagar/<minumero>&<numerodestino>&<valor>', methods=['GET'])
def pagar(minumero, numerodestino, valor):
    if not BD.existe_cuenta(str(minumero)):
        return 'No se ha encontrado la cuenta origen'
        
    elif not BD.existe_cuenta(str(numerodestino)):
        return 'No se ha encontrado la cuenta destino'
    
    if not BD.transferir(str(minumero), str(numerodestino), int(valor)):
        return 'Saldo insuficiente'
    
    date = datetime.now()
    origen = BD.get_cuenta(str(minumero)).get_id()
    saldo_origen = BD.get_cuenta(str(minumero)).get_saldo()
    destino = BD.get_cuenta(str(numerodestino)).get_id()
    saldo_destino = BD.get_cuenta(str(numerodestino)).get_saldo()

    res = f'Realizado en {date}'
    return res

@app.route('/billetera/historial/<minumero>', methods=['GET'])
def mostrar_historial(minumero):
    if(not BD.existe_cuenta(str(minumero))):
        return 'No se ha encontrado la cuenta'

    historial = BD.get_cuenta(str(minumero)).mostrar_historial()

    return historial


if __name__ == '__main__':
    app.run(debug=True)

