mydict = {'limit': 10, 'verbose': 6,"test":9}
for key, value in sorted(mydict.items(), key=lambda item: item[1]):
	print key,value
