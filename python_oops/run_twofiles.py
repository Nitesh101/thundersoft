from itertools import izip


with open("file1.txt") as textfile1, open("file2.txt") as textfile2,open("file3.txt") as textfile3: 
    for x, y,z in izip(textfile1, textfile2,textfile3):
        x = x.strip()
        y = y.strip()
	z = z.strip()
        print("{0}\t{1}\t{2}".format(x, y,z))
