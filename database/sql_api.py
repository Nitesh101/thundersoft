import sqlite3
from collections import OrderedDict


class sql_class:
	def __init__(self,name):
		print "}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}"
		print name
		print "}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}"
		self.connection = sqlite3.connect(name)
		self.cursor = self.connection.cursor()
	def execute_query(self,query):
		self.cursor.execute(query)
	def create_table(self,table_name,dict):
		heading = '('
		i = 0
		for key, value in dict.iteritems():
			heading = heading + key + ' ' + value
			i += 1
			if i < len(dict):
				heading = heading + ', '
		heading = heading + ')'
		query = 'CREATE TABLE ' + table_name + ' ' + heading
		print query
		self.execute_query(query)
		self.connection.commit()
	def insert(self,table_name, dict):
		da
