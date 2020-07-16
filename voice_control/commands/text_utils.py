import json
import random


def _normalize(str):
	''' convert cpeech text to normilized command, like 
			"включить ручное управление"
			"включить вентилятор 1"
			"положение клапан 1 (30%)"
	'''
	cmd = ''
	words = set(str.lower().split(' '))

	with open('voice_control/commands/dictionary.json', 'r', encoding='utf-8') as f:
		dictionary = json.load(f)

	first = True
	for key, value in dictionary.items():
		if set(value).intersection(words):
			if first:
				cmd += key
				first = False
			else:
				cmd += ' '
				cmd += key
	return cmd


def command_to_modbus_parameters(str):
	''' convert normalized command to set of modbus registers and thous values '''
	if not str:
		return []
		
	cmd = _normalize(str)
	params = []

	with open('voice_control/commands/commands.json', 'r', encoding='utf-8') as f:
		js = json.load(f)
	try:
		params = js[cmd]
	except KeyError:
		print('не получилось распознать комманду: \n  "%s"' %(str)) 
		raise
	return params


def get_answer(str):
	''' convert normalized command to set of modbus registers and thous values '''
	if not str:
		return 'не получилось распознать комманду'
		
	cmd = _normalize(str)
	if not cmd:
		return 'не получилось распознать комманду'

	with open('voice_control/commands/answers.json', 'r', encoding='utf-8') as f:
		js = json.load(f)
	try:
		answer = random.choice(js[cmd])
	except KeyError:
		return 'не получилось распознать комманду' 
	return answer