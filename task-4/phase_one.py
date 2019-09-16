#scripts used to understand parts of the problem

#length of plaintext
"""
n=raw_input()
l=int(len(n))
print l
print l/2
"""

#printing unicode value of ciphertext 
"""
key=raw_input()
key=key.decode("hex")
print key
"""
#unicode values of unicode
"""
&8'`): <#$")#'?*
                         %+$>#&)#5$3#6/-'8?'%	.-/(	/4;2.4-+!

           ?375!#9-/20-
?(*;
"""

#urandom
"""
from os import urandom

c = urandom(1)
print c
"""
#creation of key list to xor from given hex key
"""
hex_key="0123456789"
key_list = [hex_key[i]+hex_key[i+1] for i in range(0,len(hex_key),2)]

print key_list
"""
#xor
"""
b=int(raw_input())
c=int(raw_input())
a=b^c
print a
"""
