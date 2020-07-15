import time
from django.shortcuts import render
from .initial import executor
from .initial import client

def home(context):
	return render(context, 'voice_control/home.html')

def post_command(context):
	# execute commands
	voice_commands = [
	    'отключить ручное управление',
	    'отключить вентилятор 1'
	    ]

	for c in voice_commands:
		executor.execute(c)


	# pause 2 secs befor reading
	time.sleep(2)
	# Read words
	data = client.read_registers(2080)
	print ('readed data: %s' %(data))
	# Read floats
	data = client.read_floats(2042)
	print ('readed data: %s' %(data))

	return render(context, 'voice_control/home.html')