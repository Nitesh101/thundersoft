class parent(object):
	def __init__(self):
		self.value = 5
	def get_value(self):
		return self.value
class child(parent):
	def get_value(self):	
		return self.value + 1
c = child()
print c.get_value()
