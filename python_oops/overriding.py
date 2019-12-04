class Parent:
	def __init__(self):
		print ("this parent class constructor")
	def parentMethod(self):
		print ("thisi is parent method")
class child(Parent):
	def __init__(self):
		print ("This is child class constructo")
	#	super().__init__()
	def parentMethod(self):
	#	super().parentMethod()
		print("I'm  overriding parent calss")
obj = child()
obj.parentMethod()
