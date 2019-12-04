def add(instance,*args):
	if instance == 'int':
		result = 0
	elif instance == 'str':
		result = ''
	for i in args:
		result += i
	return  result
print add('int',2,4,5)
print add('str','I','speak','python')
