import pandas as pd
df = pd.read_csv("gain_default.csv",header=None)
data = df.drop([0,1,2,3,4])
ch = list(data[1].values)
bps = list(data[2].values)
fs = list(data[3].values)
value =list(data[9].values)
print (ch,bps,fs,value)
N = list(input("Enter 'ch' 'bps' and 'fs' values space separated ").split())


def sample(N):
	if N[0] not in ch:
		return "value Not Found"
	if N[1] not in bps:
	        return "value not found"
	if N[2] not in fs:
        	return "value not found"
	for i,j in enumerate(ch):
		if N[1]==bps[i]:
			if N[2]==fs[i]:
				return value[i]
print sample(N)
