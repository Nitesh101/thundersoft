class Parent:
	def __init__(self):
		print ("this parent class constructor")
	def parentMethod(self):
		print ("thisi is parent method")
class child(Parent):
	def __init__(self):
		print ("This is child class constructo")
		super().__init__()
	def childMethod(*args):
		print ("This is child class method")
		for arg in args:
			print (arg)
obj = child()
obj.childMethod()
obj.childMethod("Nitesh")
obj.childMethod(1,2,3)
obj.childMethod("nitesh","ramesh","suresh","satheesh")
