from modbus.client import ModbusTCPClient, ReadError, WriteError
from commands.commands import command_to_modbus_parameters

# connect to device
HOST = '10.6.2.245'
PORT = 502
print('initiate connection with %s:%s' %(HOST, PORT))
client = ModbusTCPClient(HOST, PORT)
print('connected')


'''
#Write registers
address = 1403
value = [11]
print('Write %s values at modbus address %s' %(value, address))
try:
    regs = client.writeRegisters(address, value)
except WriteError:
    print('write error')
print('finish writing')


# Read registers
address = 1403
number = 1
print('Read %s registers at modbus address %s' %(number, address))
try:
    regs = client.readRegisters(address, number)
    print ('readed data: %s' %(regs))
except ReadError:
    print('read error')
print('finish reading')
'''

'''
#Write bits
address = 15984
value = [True, True, True]
print('Write %s values at modbus address %s' %(value, address))
try:
    regs = client.writeBits(address, value)
except WriteError:
    print('write error')
print('finish writing')


# Read bits
address = 15984
number = 3
print('Read %s bits at address %s' %(number, address))
try:
    bits = client.readBits(address, number)
    print ('readed data: %s' %(bits))
except ReadError:
    print('read error')
print('finish reading')

'''

# print (command_to_modbus_parameters("выключи ручное управление"))


#Write float registers
address = 1126
value = [0]
print('Write %s float values at modbus address %s' %(value, address))
try:
    regs = client.write_floats(address, value)
except WriteError:
    print('write error')
print('finish writing')


# Read float registers
address = 52
number = 1
print('Read %s float registers at modbus address %s' %(number, address))
try:
    regs = client.read_floats(address, number)
    print ('readed data: %s' %(regs))
except ReadError:
    print('read error')
print('finish reading')