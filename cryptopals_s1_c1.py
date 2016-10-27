#!/usr/bin/python
# http://cryptopals.com/sets/1/challenges/1
# import the library to do the operations because we arent into re-inventing the wheel just yet.
import binascii
# set static variable with our challenge input
mh = '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'
# print the answer using binascii functions unhexlify and b2a_base64
# in bash we could equate this to 'echo $mh | xxd -p -r | base64'
print (binascii.b2a_base64((binascii.unhexlify(mh))))
