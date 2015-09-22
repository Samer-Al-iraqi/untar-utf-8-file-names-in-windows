# require Python 2 installed on Windows

import tarfile
import codecs
import sys

def recover(name):
	return codecs.decode(name,"utf-8")

# TarPath is the path of tar file (e.g. G:\sda8.tar)
tar = tarfile.open('TarPath', mode='r', bufsize=16*1024)
updated = []
print ('Finish creating tar object') 
for m in tar.getmembers():
	m.name = recover(m.name)
	updated.append(m)
print ('Finish creating files lists with updated names')
# put here the path for the directory that will contain the extracted files (e.g E:\somedir\)
tar.extractall(path="path", members=updated)
tar.close()
print ('finish Evertying') 
