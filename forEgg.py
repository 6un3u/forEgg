from sys import argv
from struct import unpack

#get full length of file
def getsize(f):
	f.seek(0,2)
	size = f.tell()
	return size
	
#get length of filename
def name_length(p):
	f.seek(p)
	print(f.tell())
	size = f.read(2)
	print(size)
	size = int.from_bytes(size, byteorder='big')
	return size
	

f = open(argv[1], 'rb')
b = f.read()
fsize = getsize(f)

#the magic num of filenameHeader in Egg format
magic = b'\xac\x91\x85\n'

f.seek(0)
while True:
	b = f.read(1)
	p = f.tell()

	if b == b'':
		break
	
	if b == magic[:1]:
		f.seek(p-1)
		b = f.read(4)
		p = f.tell()
		
					
		if b == magic:
			size = name_length(p)
			f.read(1)			
			name = f.read(size)
			name = name.decode('utf-8')
			print(name)
			
		
f.close()
