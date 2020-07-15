from .text_utils import command_to_modbus_parameters
from modbus.client import ReadError, WriteError
from utils import utils

class ParameterTypeError(Exception):
	pass

class VoiceCommandExecutor():
	def __init__(self, modbus_client, logger):
		self.client = modbus_client
		self.logger = logger

	def execute(self, command):
		self.logger.debug('executing command: %s' %(command))
		set_parameters = command_to_modbus_parameters(command)
		self.logger.debug('executing parameters: %s' %(set_parameters))
		for p in set_parameters:
			self._set_modbus_parameter(p)
		self.logger.debug('executing done')

	def _set_modbus_parameter(self, parameter):
		# parameter is dictionari like { "type": "real", "addr": 2042, "value": 100 }
		if parameter['type'] in ('float', 'real'):
			self._set_modbus_float(parameter['addr'], [parameter['value']])
		elif parameter['type'] == "word":	
			self._set_modbus_word(parameter['addr'], [parameter['value']])
		elif parameter['type'] == "bool":
			adr = parameter['addr']
			if type(adr) is str:
				adr = int(utils.register_to_bit(adr))
			self._set_modbus_bits(adr, [parameter['value']])
		else:
			raise ParameterTypeError(parameter)

	def _set_modbus_word(self, address, values):
		''' 
		address = 1403
		values = [11, 2, 25] 
		'''
		self.client.write_registers(address, values)
		return True

	def _set_modbus_float(self, address, values):
		''' 
		address = 1200
		values = [0.3, 2.7, 100.69] 
		'''
		self.client.write_floats(address, values)
		return True

	def _set_modbus_bits(self, address, values):
		''' 
		address = 16
		values = [True, False, True] 
		'''
		self.client.writ_bits(address, values)
		return True