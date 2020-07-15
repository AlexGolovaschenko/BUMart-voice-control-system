import logging
from .modbus.client import ModbusTCPClient
from .commands.execution import VoiceCommandExecutor


# get logger
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger('main')
# logger.addHandler(logging.StreamHandler())
logger.debug('Programm started')


# connect to device
HOST = '10.6.2.245'
PORT = 502
client = ModbusTCPClient(HOST, PORT, logger)


# create command executor
executor = VoiceCommandExecutor(client, logger)





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
