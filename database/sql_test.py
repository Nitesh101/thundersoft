import sqlite3
from employee import Employee

conn = sqlite3.connect("employee.db")

c = conn.cursor()
#c.execute("""CREATE TABLE nitesh (
#		first text,
#		last text,
##		pay integer
#		)""")

def insert_emp(emp):
	with conn:
		c.execute("INSERT INTO nitesh VALUES (?,?,?)",(emp.first,emp.last,emp.pay))


def get_emps_by_name(lastname):
	c.execute("SELECT * FROM nitesh WHERE last=:last",{'last':lastname})
	return c.fetchall()

def update_pay(emp,pay):
	with conn:
		c.execute("""UPDATE nitesh SET pay = :pay
				WHERE first = :first AND last = :last""",
				{'first': emp.first,'last':emp.last,'pay':pay})
def remove(emp):
	with conn:
		c.execute("DELETE from nitesh WHERE first = :first AND last = :last",{'first':emp.first,'last':emp.last})


emp_1 = Employee('John','Deo',90000)
emp_2 = Employee('Jane','Deo',80000)


#insert_emp(emp_1)
#insert_emp(emp_2)
emps = get_emps_by_name('Deo')
print emps

#remove(emp_1)
#remove(emp_2)

emps = get_emps_by_name('Deo')
print emps

conn.close()










