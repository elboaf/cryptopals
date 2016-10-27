#!/usr/bin/python
import binascii
import math
mh = '1c0111001f010100061a024b53535009181c'
mx = '686974207468652062756c6c277320657965'
answer = []

if len(mh) == len(mx):
	dh = list(binascii.unhexlify(mh))
	dx = list(binascii.unhexlify(mx))
	for num in range(0,len(binascii.unhexlify(mh))):
		answer.append(dh.pop() ^ dx.pop())
	answer.reverse()
#	for x in answer:
#		print(''.join(hex(x)[2:]))

	print (''.join([hex(i)[2:] for i in answer]))
else:
	print('yo dj, we got a length mismatch!')

