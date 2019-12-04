class Dog:
	species = "animal"
	def __init__(self,name,age):
		self.name = name
		self.age = age
	def description(self):
		return "{} is {} years old".format(self.name,self.age)
	def speak(self,sound):
		return "{} says {}".format(self.name,sound)
mikey = Dog("mikey",5)
print(mikey.description())
print(mikey.speak("dnsajdna"))
print mikey.__class__.species
