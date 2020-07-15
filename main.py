import logging
import time
from modbus.client import ModbusTCPClient
from commands.execution import VoiceCommandExecutor


# get logger
logging.basicConfig(filename='log.txt', level=logging.DEBUG)
logger = logging.getLogger('main')
logger.addHandler(logging.StreamHandler())
logger.debug('Programm started')


# connect to device
HOST = '10.6.2.245'
PORT = 502
client = ModbusTCPClient(HOST, PORT, logger)


# execute commands
voice_commands = [
    'включить ручное управление',
    'включить вентилятор 1'
    ]

ex = VoiceCommandExecutor(client, logger)
for c in voice_commands:
    ex.execute(c)

# pause 2 secs befor reading
time.sleep(2)
# Read words
data = client.read_registers(2080)
print ('readed data: %s' %(data))
# Read floats
data = client.read_floats(2042)
print ('readed data: %s' %(data))


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
number = 1
bits = client.readBits(address, number)
print ('readed data: %s' %(bits))

'''
'''
import speech_recognition as sr

# obtain audio from the microphone
r = sr.Recognizer()
with sr.Microphone() as source:
    print("Say something!")
    audio = r.listen(source)

# recognize speech using Google Speech Recognition
try:
    # for testing purposes, we're just using the default API key
    # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
    # instead of `r.recognize_google(audio)`
    text = r.recognize_google(audio, language='ru')
    print("Google Speech Recognition thinks you said " + text)
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))

print (command_to_modbus_parameters(text))
'''
