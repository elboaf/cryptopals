#!/usr/bin/env python
import binascii

def ranxor(mh,mx):
	# static xor for brute forcing key s1c3
	# with scoring system to find english words
	# using ascii table, heres how i want to try scoring:
	# decimal 0 - 31 or 127 should be failure/discarded
	# decimal 127 and higher should be failure/discarded
	answer = []
	dh = list(binascii.unhexlify(mh))
	for num in range(0,len(binascii.unhexlify(mh))):
		answer.append(dh.pop() ^ mx)
		if answer.copy().pop() < 32:
			return 0;
		if answer.copy().pop() > 126:
			return 0;
	answer.reverse()
	out=(''.join([hex(i)[2:] for i in answer]))
	return out;

def c3(low,high,string):
	answer = []
	for x in range(low,high):

		if not(ranxor(string,x))== 0:
			#print ('string = ', string,'key = ', chr(x))
			print(binascii.unhexlify(ranxor(string,x)))
	return 0;

def c4(file):
	answer=[]
	f1 = open(file)
	f1_line = (f1.read())
	for x in f1_line.splitlines():
		answer.append(c3(0,256, x))
		#print(c3(0,255,x))
	return answer;

print(c4('4.txt'))

