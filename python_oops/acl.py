import os
def acl():
	log = open("file.log","a")
	try:
		f=os.access("new.txt",os.R_OK)
		log.write("acl      PASS\n")
	except:
		log.write("acl      FAIL\n")
	log.close()
if __name__=="__main__":
	acl()
