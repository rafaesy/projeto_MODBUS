from cliente.cliente_modbus import ClienteMODBUS

cliente = ClienteMODBUS(
    '127.0.0.1',
    502
)

cliente.conecta()

cliente.escreveFloat(
    2000,
    15.7
)

valor = cliente.lerFloat(2000)

print("Valor lido:", valor)

cliente.close()