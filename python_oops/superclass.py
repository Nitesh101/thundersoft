class parent(object):
	def __init__(self):
		print "DsdD"
		pass
class child(parent):
	def __init__(self):
		super(child,self).__init__()
		print "DASDADA"
obj = child()
