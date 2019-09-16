#this was the first brute force method that tried all possible combinations from AAAAA to zzzzz as keys and then decrypted the ciphertext using the same encryption method as inverse of xor function is xor itself, then compared the plaintext generated.
#this method has a very minute chance of guessing the correct key

import hashlib
from ctypes import CDLL

a=raw_input()
uniarr=a.decode("hex")
n=0
plaintext=""
for i in range(65,91) + range(97, 123):
    for j in range(65,91)+ range(97, 123):
        for k in range(65,91)+ range(97, 123):
            for l in range(65,91)+ range(97, 123):
                for m in range(65,91)+ range(97, 123):
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
                    if n==1:
                        break
                if n==1:
                    break
            if n==1:
                break
        if n==1:
            break
    if n==1:
        break
print "-----------------------------------------------------------------------"
print ans
print k
