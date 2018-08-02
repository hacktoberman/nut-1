
class File:
	def __init__(self, path = None, mode = None):
		self.offset = 0
		self.size = None
		self.f = None
		if path:
			self.open(path, mode)
			
	def partition(self, offset = 0, size = None, n = None):
		if not n:
			n = File()
		#print('partition: ' + str(self) + ', ' + str(n))
			
		n.offset = self.offset + offset
		
		if not size:
			size = self.size - n.offset - self.offset
			
		n.size = size
		n.f = self
		
		return n
		
	def read(self, size):
		return self.f.read(size)
		
	def readInt8(self, byteorder='little', signed = False):
		return self.f.read(1)
		
	def readInt16(self, byteorder='little', signed = False):
		return int.from_bytes(self.f.read(2), byteorder=byteorder, signed=signed)
		
	def readInt32(self, byteorder='little', signed = False):
		return int.from_bytes(self.f.read(4), byteorder=byteorder, signed=signed)
		
	def readInt64(self, byteorder='little', signed = False):
		return int.from_bytes(self.f.read(8), byteorder=byteorder, signed=signed)
		
	def write(self, buffer):
		return self.f.write(buffer)
	
	def seek(self, offset, from_what = 0):
		#print('seeking: ' + str(self.f) + ', ' + str(self))
		if not self.isOpen():
			raise IOError('Trying to seek on closed file')
		#if self.parent:
		#	f = self.parent
		#else:
		#	f = self.f
		f = self.f

		if from_what == 0:
			# seek from begining
			return f.seek(self.offset + offset)
		#elif from_what == 1:
			# seek from current position
		#	pass
		elif from_what == 2:
			# see from end
			if offset > 0:
				raise Exception('Invalid seek offset')
				
			return f.seek(self.offset + offset + self.size)
			
		raise Exception('Invalid seek type')
		
	def open(self, path, mode):
		if self.isOpen():
			self.close()
			
		self.f = open(path, mode)
		
		self.f.seek(0,2)
		self.size = self.f.tell()
		self.f.seek(0,0)
		
	def close(self):
		self.f.close()
		self.f = None
		
	def tell():
		return self.f.tell()
		
	def isOpen(self):
		return self.f != None