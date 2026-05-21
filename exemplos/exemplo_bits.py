from cliente.cliente_modbus import ClienteMODBUS

cliente = ClienteMODBUS(
    '127.0.0.1',
    502
)

cliente.conecta()

bits = cliente.lerBits(1000)

print("Bits antes:")
print(bits)

cliente.escreveBit(
    1000,
    3,
    1
)

bits = cliente.lerBits(1000)

print("Bits depois:")
print(bits)

cliente.close()