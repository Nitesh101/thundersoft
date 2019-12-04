class Employee:
	num_of_emps = 0
	raise_amount = 1.04
	def __init__(self,first,last,pay):
		self.first = first	
		self.last = last
		self.pay = pay
		self.email = first+'.'+last+'@company.com'
		
		Employee.num_of_emps += 1
	def fullname(self):
		return '{} {}'.format(self.first,self.last)
	def apply_raise(self):
		self.pay = int(self.pay * self.raise_amount)
emp1 = Employee('nitesh','veera',50000)
emp2 = Employee('test','user',60000)




print Employee.raise_amount
print emp1.raise_amount
print emp2.raise_amount



#ieggy.run()

#emp1.raise_amount = 1.05
#print emp1.__dict__
#print emp1.pay
#emp1.apply_raise()
#print Employee.raise_amount
#print emp1.pay
#print "==================="
#print emp1.pay
#emp2.apply_raise()
#print emp2.pay
