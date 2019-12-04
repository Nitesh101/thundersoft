"""
class parent:
	def __init__(self,fname,age):
		self.fname = fname
		self.age = age
	def view(self):
		print(self.fname,self.age)
class child(parent):
	def __init__(self,fname,age):
		parent.__init__(self,fname,age)
		self.lastname = "Edureka"
	def view(self):
		print (self.fname,self.lastname,self.age)
ob = child("python",20)
ob.view()
"""
class parent:
	def __init__(self,fname,age):
		self.fname = fname
		self.age = age
	def view(self):
		print(self.fname ,self.age)
class child(parent):	
	def __init__(self,fname,age,lastname):	
		parent.__init__(self,fname,age)
		self.lastname = lastname 
	def view(self):
		print self.fname,self.age,self.lastname
d = child('python',30,'edureka')
d.view()
