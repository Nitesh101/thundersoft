class Employee:
	def __init__(self,first,last,pay):
		self.first = first 
		self.last = last
		self.pay = pay
		self.email = first + '.' + last + '@company.com'
	def full_name(self):
		return "{} {}".format(self.first,self.last)
emp1 = Employee('nitesh','veera',3000)
emp2 = Employee('test','user',4000)
print emp1.email
print emp2.email
print emp1.full_name()
print emp2.full_name()
