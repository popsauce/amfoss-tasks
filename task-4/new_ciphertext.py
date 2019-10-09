import hashlib
from ctypes import CDLL
"""
print "Enter the ciphertext you want to decrypt."
a=raw_input()
"""
a="2a2138440b1c233d080d072b29441c1b2b6d250c052f23070d176e152b3a"
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
                                        if hashlib.md5(flag).digest().encode("hex") == "067abbb88d2201a393ba660728f83b84":
                                            print "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
                                            print "Yeah!....You are a genius!"
                                            print ""
                                            ans=value
                                            fin=flag
                                            br=1
                                        
print ans
print ""
print fin
