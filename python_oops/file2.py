class car(object):
	def __init__(self,model,colour,company,speed_limit):
		self.colour = colour
		self.company = company
		self.model = model
		self.speed_limit = speed_limit
	def car_detais(self):
		return self.model,self.colour,self.company,self.speed_limit
	def start(self):
		print("started")
	def stop(self):
		print("stopped")
	def accelarate(self):
		print ("acclarating.....")
	def change_gear(self,gear_type):
		print("gear changed")
maruthi = car("eritiga","black","suzuki",50)
audi = car("A6","Red","audi",120)
print maruthi.car_detais()
print audi.car_detais()
maruthi.start()
maruthi.change_gear(2)
