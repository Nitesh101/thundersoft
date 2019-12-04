class bear(object):
	def sound(self):
		print "Groarrr"
class dog(object):
	def sound(self):
		print "wooff woof"
	def makesound(self,animalType):
		animalType.sound()
bearobj = bear()
dogobj = dog()
makesound(bearobj)
makesound(dogobj)
