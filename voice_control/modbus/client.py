from pyModbusTCP.client import ModbusClient
from pyModbusTCP import utils


class ReadError(Exception):
    pass
class WriteError(Exception):
    pass

class ModbusTCPClient():
	BIG_ENDIAN = False

	def __init__(self, host, port, logger, *args, **kwargs):
		self.logger = logger
		try:
			self.client = ModbusClient(host=host, port=port, auto_open=True)
			try:
				self.client.timeout(kwargs['timeout'])
			except:
				pass
		except ValueError:
			self.logger.error("Connection failed. Error with host or port params = %s:%s" %(host, port))
			raise
		self.logger.debug('connected to %s:%s' %(host, port))


	def read_registers(self, addr, namber=1):
		regs_list = self.client.read_holding_registers(addr, namber)
		if regs_list:
		    return(regs_list)
		else:
		    raise ReadError()

	def read_floats(self, addr, number=1):
		reg_l = self.read_registers(addr, number * 2)
		return [utils.decode_ieee(f) for f in utils.word_list_to_long(reg_l, big_endian=self.BIG_ENDIAN)]


	def read_bits(self, bit_addr, bit_namber=1):
		bits_list = self.client.read_coils(bit_addr, bit_namber)
		if bits_list:
		    return(bits_list)
		else:
		    raise ReadError()

	def write_registers(self, addr, values):
		if self.client.write_multiple_registers(addr, values):
		    return True
		else:
		    raise WriteError()

	def write_bits(self, bits_addr, bits_value):
		if self.client.write_multiple_coils(bits_addr, bits_value):
		    return True
		else:
		    raise WriteError()

	def write_floats(self, address, floats_list):
		b32_l = [utils.encode_ieee(f) for f in floats_list]
		b16_l = utils.long_list_to_word(b32_l, big_endian=self.BIG_ENDIAN)
		return self.write_registers(address, b16_l)