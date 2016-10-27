#!/usr/bin/python
# http://cryptopals.com/sets/1/challenges/2
# need unhexlify function from binascii
import binascii
# static varibales with our equal-length strings from challenge
mh = '1c0111001f010100061a024b53535009181c'
mx = '686974207468652062756c6c277320657965'
# initialize array called answer
answer = []
# check that our inputs are equal length
if len(mh) == len(mx):
	# hex decode each input, create a stack/buffer for each using list function
	dh = list(binascii.unhexlify(mh))
	dx = list(binascii.unhexlify(mx))
	# for the length of our input..
	for num in range(0,len(binascii.unhexlify(mh))):
		# xor each corresponding byte from right to left using pop() and output to our array
		answer.append(dh.pop() ^ dx.pop())
	# since our stack is lifo, our answer is backwards, reverse it with reverse()	
	answer.reverse()
# now we need to join our array back into a representation/format that conforms to the challenge requirements
# we will use the join function, and hex() function, with pretty printing using [2:] (hides the 0x prefix)

# this loop i wrote, but it has a problem. it invokes print on each iteration, and has the consequence of printing each result 
# on a new line.
#
#	for x in answer:
#		print(''.join(hex(x)[2:]))
#
# this next line i borrowed from some example on stack overflow. 
# its nice because it invokes print only once, and prints the results one after another on the same line. this is what we want ^_^
	print (''.join([hex(i)[2:] for i in answer]))
else:
	# this line is printed if our inputs dont match, which will be needed when we convert this script into a function
	print('yo dj, we got a length mismatch!')

