#!/usr/bin/python
import binascii
s1 = '1c0111001f010100061a024b53535009181c'
s2 = '686974207468652062756c6c277320657965'
s3 = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'
def hexor(mh,mx):
	# hex string xor s1c2
	answer = []
	if len(mh) == len(mx):
		dh = list(binascii.unhexlify(mh))
		dx = list(binascii.unhexlify(mx))
		for num in range(0,len(binascii.unhexlify(mh))):
			answer.append(dh.pop() ^ dx.pop())
		answer.reverse()
		out=(''.join([hex(i)[2:] for i in answer]))
		return out;


def fuxor(mh,mx):
	# static xor for brute forcing key s1c3
	answer = []
	dh = list(binascii.unhexlify(mh))
	for num in range(0,len(binascii.unhexlify(mh))):
		answer.append(dh.pop() ^ mx)
	answer.reverse()
	out=(''.join([hex(i)[2:] for i in answer]))
	return out;

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

for x in range(0,255):
	out=(ranxor(s3,x))
	if out == 0:
		pass
	else:
		print(binascii.unhexlify(out))
