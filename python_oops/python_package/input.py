import sys
sys.path.append('/home/nitesh/Desktop/my_modules')
from my_module import find_index,test


courses = ['History','Matth','social','sceience']
index = find_index(courses,'Math')
print index
print test
print sys.path
