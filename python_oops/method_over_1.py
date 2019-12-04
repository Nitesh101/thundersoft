class test:	
	def sayhello(self,name=None):
		if name is not None:
			print ("Hello" + name)
		else:
			print "hello"
o = test()
o.sayhello()
o.sayhello('Guido')
