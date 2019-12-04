class person(object):
	def __init__(self,name):
		self.name = name
	def getName(self):
		return self.name
	def isEmployee(self):
		return False
class Employee(person):
	def isEmployee(self):
		return True
emp = person("test")
print emp.getName(),emp.isEmployee()
emp2 = Employee("user")
print emp2.getName(),emp2.isEmployee()
