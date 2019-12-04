class parent():
	def first(self):
		print("first function")
class child(parent):
	def second(self):
		print("second functtion")
f = child()
f.first()
f.second()
