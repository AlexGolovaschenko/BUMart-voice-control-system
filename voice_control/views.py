import time
from django.shortcuts import render, redirect
from django.contrib import messages
from voice_control.initial import executor, client, logger
from voice_control.modbus.client import WriteError

def home(request):
	return render(request, 'voice_control/home.html')

def post_command(request):
	voice_command = str(request.POST.get('command', ''))
	logger.debug('accepted command: ' + voice_command)
	answer = _execute_commands(voice_command)
	messages.add_message(request, messages.INFO, answer)
	return redirect('voice:home')


def _execute_commands(command):
	# execute commands
	answer = 'здесь ничего нет'
	try:
		answer = executor.execute(command)
	except WriteError:
		#try again 
		logger.debug('modbus write attempt 2')
		time.sleep(0.5)
		try:
			answer = executor.execute(command)
		except WriteError:
			#try again 
			logger.debug('modbus write attempt 3')
			time.sleep(0.5)
			try:
				answer = executor.execute(command)
			except WriteError:
				logger.debug('modbus write error')
				answer = 'Ошибка записи регистров модбас'
	except KeyError:
		answer = 'Команда не распознана'

	logger.debug('executing commands')
	return answer
