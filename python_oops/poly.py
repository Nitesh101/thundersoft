class India():
	def capital(self):
		print "New Delhi is the capital of India"
	def language(self):
		print "Hindhi the primaty langage of india"
	def type(self):
		print "India is developing country"
class usa():
	def capital(self):
		print"washington D.C"
	def language(self):
		print "Ebglish"
	def type(self):
		print "Develloped country"
obj1 = India()
obj2 = usa()
for country in (obj1,obj2):
	country.capital()
	country.language()
	country.type()
