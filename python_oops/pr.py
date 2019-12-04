'This is docstring'
class test:	
	def __init__(self,x,y,z):
		'This is test intilizer with coordinate'
		self.x = x
		self.y = y
		self.z = z
	def printpoint(self):
		'this method print the value'
		print (self.x,self.y,self.z)
print (__doc__)
p1 = test(2,3,4)
#p1.printpoint()
print(p1.__init__.__doc__)
print(p1.printpoint.__doc__)
