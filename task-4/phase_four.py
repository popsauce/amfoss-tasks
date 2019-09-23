#based on the output strings analysed in phase three, following changes were made:

import hashlib
from ctypes import CDLL

a=raw_input()
uniarr=a.decode("hex")
n=0
plaintext=""
for i in range(70,71) + range(72,73)+ range(74,78)+ range(79,80)+ range(83,84)+ range(102,103)+ range(104,105)+ range(106,110)+ range(111,112)+ range(115,116):
    if n==1:
        break
    for j in range(65,66)+ range(70,72)+ range(74,78)+ range(81,82)+ range(84,88)+ range(97,98)+ range(102,104)+ range(106,110)+ range(113,114)+ range(116,120):
        if n==1:
            break
        for k in range(68,69)+ range(71,74)+ range(76,79)+ range(82,84)+ range(85,86)+ range(87,90)+ range(100,101)+ range(103,106)+ range(108,110)+ range(114,116)+ range(117,118)+ range(119,122):
            if n==1:
                break
            for l in range(65,66)+ range(67, 68)+ range(70,73)+ range(74,77)+ range(80,83)+ range(86,88)+ range(97,98)+ range(99,100)+ range(102,105)+ range(106,109)+ range(112,115)+ range(118,120):
                if n==1:
                    break
                for m in range(70,71)+ range(74,75)+ range(76,79)+ range(80,82)+ range(89,91)+ range(102,103)+ range(106,107)+ range(108,111)+ range(112,114)+ range(121,123):
                    if n==1:
                        break
                    a=chr(i)
                    b=chr(j)
                    c=chr(k)
                    d=chr(l)
                    e=chr(m)
                    key=a+b+c+d+e
                    print ""
                    print key
                    print ""
                    hex_key = key.encode("hex")
                    key_list = [hex_key[a]+hex_key[a+1] for a in range(0,len(hex_key),2)]
                    for n in xrange(len(uniarr)):
                        plaintext += chr(ord(uniarr[n]) ^ int(key_list[i%5], 16))
                    
                    flag="{"+plaintext+"}"
                    if hashlib.md5(flag).digest().encode("hex") == "d444d1ac3799a86d31f34b4a8a3243c6":
                        ans=flag
                        k=key
                        n=1
                    
print "-----------------------------------------------------------------------"
print ans
print k
