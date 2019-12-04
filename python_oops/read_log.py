import re
file = 'file.log'

lis = []
def read_log(file):
	global key_word
	with open(file) as f_obj:
		dat = f_obj.readlines()
		key_word = "API_Gstreamer_log"
	for line in dat:
		if key_word in line:
			sa =  line.split()
			sa = ''.join(sa[1])
			val = re.findall(r'\d{2}',sa)
			lis.append(''.join(val))
		
read_log(file)
def find_avg(lis):
	da = [int(i) for i in lis]
	print  key_word ,":" ,sum(da) /len(da)
find_avg(lis)

"""
import re
global lis
def read_log(file):
	global keyword
	with open(file) as d:
		data = d.readlines()
	lis = []
	keyword = 'API_Gstreamer_log'
	#keyword  = raw_input("Enter API name to get Avg ")
	for line in data:
		#keyword = raw_input("Enter Api name to get avg: ")
		if keyword in line:
			st = line.split()
			#print st[1]
			fa = ''.join(st[1])
			value = re.findall(r'\d{2}',fa)
			t = ''.join(value)
			lis.append(t)
	return lis
lis = read_log('file.log')
def find_avg(lst):
	final = []
	for i in lst:
		ta = int(i)
		final.append(ta)
	data = sum(final) / len(final)
	print  keyword , ":" , data
find_avg(lis)
"""
