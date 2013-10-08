class Packet:
	def __init__(self, data):
		self.data = data
		self.opcode = self.data[:2]
		self.data = self.data[2:]

class ACK(Packet):
	"""
	Structure that describes and serializes an ACK packet.
	"""
	def __init__(self, data):
		super().__init__(self, data)


	def __str__(self):



class DATA(Packet):
	"""
	Structure that describes and serializes a DATA packet.
	"""
	def __init__(self, data):
		super().__init__(self, data)

	def __str__(self):

class RRQ(Packet):
	"""
	Structure that describes and serializes a RRQ packet.
	"""
	def __init__(self, data):
		super().__init__(self, data)
		self.filename = data[:data.find("\0")]
		self.data = self.data[data.find("\0")+1:]



	def __str__(self):

class WRQ(Packet):
	"""
	Structure that describes and serializes a WRQ packet.
	"""
	def __init__(self, data):
		super().__init__(self, data)
		self.filename = data[:data.find("\0")]
		self.data = self.data[data.find("\0")+1:]

	def __str__(self):

class ERROR(Packet):
	"""
	Structure that describes and serializes an ERROR packet.
	"""
	def __init__(self, data):
		super().__init__(self, data)

	def __str__(self):
