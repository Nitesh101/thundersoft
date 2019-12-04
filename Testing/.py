import re
def get_memory(file):
	with open(file) as f:
		data = f.readlines()
	key_word = ["QSR_STR"]
	out = {}
	for line in data:
		if all(sub_str in line for sub_str in key_word):
			st = line.split()
			print st
			global hex_value
			hex_value = st[2:3]
			key_value = st[-2].split('/')[-1].split('(')[0]
			print key_value
			try:
				out[key_value].append(hex_value)
			except KeyError:
				out[key_value] = []
				out[key_value].append(hex_value)
	return out
f_obj =  open("ouuutt.txt","w") 
for key,value in get_memory("New Text Document (2).txt").items():
	lis = []
	for hex_value in value:
		sa =  ''.join(hex_value)
		if re.findall(r'0x.*',sa):
			ta = int(sa,16)
			lis.append(ta)
	ts = sum(lis)
	f_obj.write('{} '.format(key))
	f_obj.write('{}\n'.format(ts))
