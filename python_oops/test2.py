class method():
	def demo(self,name=None , age=None):
		if (name != None and age != None):
			print ("name:",name,"age:",age)
		elif (name == None):
			print("Age is:",age)
		elif (age == None):
			print("My name is :" ,name)
		else:
			print "there is no data"

obj = method()
obj.demo("nitesh")
obj.demo("nitesh",20)
obj.demo()
