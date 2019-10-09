from os import urandom
import hashlib
from ctypes import CDLL
import string

"""
old ciphertext="05181c2638270301601329023a203c2324072229230401273f2a1b0b02252b071e243e2313262923352411332336031b2f2d27191602383f07062e0827041725092e161e2d2f281017092f34123b321e2e12342d2b210c0b0e3f191f33370f1935000e2123392d132f163213152308302d0a0f3f282a0e183b"
old conditions= flag within curly braces
new ciphertext="2a2138440b1c233d080d072b29441c1b2b6d250c052f23070d176e152b3a"
new conditions= flag is without curly braces
"""
checkervalue=""

encrypt=raw_input("Do you want to encrypt and then decrypt your own plaintext ? [Y/N]")

if encrypt=="Y":
    key = ""
    ciphertext = ""
    def get_key():
        global key
        c = urandom(1)
        if len(key)!=5:
            if c not in string.ascii_lowercase and c not in string.ascii_uppercase :
                get_key()
            else:
                key += c
                get_key()
    
    def xor_encrypt(x):
        global key
        global ciphertext
        get_key()
    
        hex_key = key.encode("hex")
        key_list = [hex_key[i]+hex_key[i+1] for i in range(0,len(hex_key),2)]
        print "This is the key that has been used for encryption generated using urandom :- "
        print key
        print ""
        for i in xrange(len(x)):
            ciphertext += chr(ord(x[i]) ^ int(key_list[i%5], 16))

    
    if __name__ == "__main__":
        plaintext = raw_input("Enter the plaintext to be encrypted: ")
        checkervalue==plaintext
        xor_encrypt(plaintext)
        print "This is your ciphertext (encrypted plaintext). :-"
        print ciphertext.encode("hex")
        print ""
elif encrypt=="N":    
    print "This is the current ciphertext:2a2138440b1c233d080d072b29441c1b2b6d250c052f23070d176e152b3a"   

print "Enter the ciphertext you want to decrypt."
a=raw_input()
a=a.decode("hex")
l=len(a)
loflist=int(l/5)
extravalue=l-loflist

lofcipone=loflist
lofciptwo=loflist
lofcipthree=loflist
lofcipfour=loflist
lofcipfive=loflist

if extravalue==1 or extravalue==2 or extravalue==3 or extravalue==4:
    lofcipone=lofcipone+1
if extravalue==2 or extravalue==3 or extravalue==4:
    lofciptwo=lofciptwo+1
if extravalue==3 or extravalue==4:
    lofcipthree=lofcipthree+1
if extravalue==4:
    lofcipfour=lofcipfour+1

cipone=[]
ciptwo=[]
cipthree=[]
cipfour=[]
cipfive=[]

i=0
b=0
while i<lofcipone:
    cipone.append(ord(a[b]))
    b=b+5
    i=i+1
i=0
b=1
while i<lofciptwo:
    ciptwo.append(ord(a[b]))
    b=b+5
    i=i+1
i=0
b=2
while i<lofcipthree:
    cipthree.append(ord(a[b]))
    b=b+5
    i=i+1
i=0
b=3
while i<lofcipfour:
    cipfour.append(ord(a[b]))
    b=b+5
    i=i+1
i=0
b=4
while i<lofcipfive:
    cipfive.append(ord(a[b]))
    b=b+5
    i=i+1

print " These five lists represent 5 cipherlists :"

print cipone
print ciptwo
print cipthree
print cipfour
print cipfive

checkpoint=raw_input("Do you want to continue ? ...")

br=0
for aa in range(65,91)+ range(97,123):
    if br==1:
        break
    loopone=0
    plaone=""
    for i in cipone:
        x=aa^i
        if x>=32 and x<=126:
            plaone+=chr(x)
        else:
            plaone=""
            loopone=1
            break
    if loopone!=1:
        for ab in range(65,91)+range(97,123):
            if br==1:
                break
            looptwo=0
            platwo=""
            for j in ciptwo:
                x=ab^j
                if x>=32 and x<=126:
                    platwo+=chr(x)
                else:
                    platwo=""
                    looptwo=1
                    break
            if looptwo!=1:
                for ac in range(65,91)+ range(97,123):
                    if br==1:
                        break
                    loopthree=0
                    plathree=""
                    for k in cipthree:
                        x=ac^k
                        if x>=32 and x<=126:
                            plathree+=chr(x)
                        else:
                            plathree=""
                            loopthree=1
                            break
                    if loopthree!=1:
                        for ad in range(65,91)+range(97,123):
                            if br==1:
                                break
                            loopfour=0
                            plafour=""
                            for l in cipfour:
                                x=ad^l
                                if x>=32 and x<=126:
                                    plafour+=chr(x)
                                else:
                                    plafour=""
                                    loopfour=1
                                    break
                            if loopfour!=1:
                                for ae in range(65,91)+range(97,123):
                                    if br==1:
                                        break
                                    loopfive=0
                                    plafive=""
                                    for m in cipfive:
                                        x=ae^m
                                        if x>=32 and x<=126:
                                            plafive+=chr(x)
                                        else:
                                            plafive=""
                                            loopfive=1
                                            break
                                    if loopfive!=1:
                                        plaintext=""
                                        aaa=chr(aa)
                                        aab=chr(ab)
                                        aac=chr(ac)
                                        aad=chr(ad)
                                        aae=chr(ae)
                                        value=aaa+aab+aac+aad+aae
                                        print value
                                        for a in range(0,lofcipfive):
                                            plaintext+=plaone[a]+platwo[a]+plathree[a]+plafour[a]+plafive[a]
                                        
                                        if lofcipone>lofcipfive:
                                            plaintext=plaintext+plaone[lofcipfive]
                                        if lofciptwo>lofcipfive:
                                            plaintext=plaintext+platwo[lofcipfive]
                                        if lofcipthree>lofcipfive:
                                            plaintext=plaintext+plathree[lofcipfive]
                                        if lofcipfour>lofcipfive:
                                            plaintext=plaintext+plafour[lofcipfive]
                                        
                                        flag=plaintext
                                        print ""
                                        print flag
                                        print ""
                                        if checkervalue=="":
                                            if hashlib.md5(flag).digest().encode("hex") == "067abbb88d2201a393ba660728f83b84":
                                                print "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
                                                print "Yeah!....You are a genius!"
                                                print ""
                                                ans=value
                                                fin=flag
                                                br=1
                                        else:
                                            if flag==checkervalue:
                                                print "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
                                                print "Yeah!....You are a genius!"
                                                print ""
                                                ans=value
                                                fin=flag
                                                br=1
print ans
print ""
print fin
