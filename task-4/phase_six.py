import hashlib
from ctypes import CDLL

plainfirst=""
plainsecond=""
plainthird=""
plainfourth=""
plainfifth=""
a="05181c2638270301601329023a203c2324072229230401273f2a1b0b02252b071e243e2313262923352411332336031b2f2d27191602383f07062e0827041725092e161e2d2f281017092f34123b321e2e12342d2b210c0b0e3f191f33370f1935000e2123392d132f163213152308302d0a0f3f282a0e183b"
a=a.decode("hex")

listone=[70,72,74,75,76,77,79,83,102,104,106,107,108,109,111,115]
listwo=[65,70,71,74,75,76,77,81,84,85,86,87,97,102,103,106,107,108,109,110,114,115,117,119,120,121]
listhree=[68,71,72,73,76,77,78,82,83,85,87,88,89,100,103,104,105,108,109,110,114,115,117,119,120,121]
listfour=[65,67,70,71,72,74,75,76,80,81,82,86,87,97,99,102,103,104,106,107,108,112,113,114,118,119]
listfive=[70,74,76,77,78,80,81,89,90,102,106,108,109,110,112,113,121,122]
for aa in listone:
    for i in range(0,125,5):
        p=ord(a[i])
        x=aa^p
        if x>=48 and x<=90 and x>=97 and x<=123:
            plainfirst+=x
        else:
            break
    for ab in listwo:
        for i in range(1,121,5):
            q=ord(a[i])
            x=ab^q
            if x>=48 and x<=90 and x>=97 and x<=123:
                plainsecond+=x
            else:
                break    
        for ac in listhree:
            for i in range(2,122,5):
                r=ord(a[i])
                x=ac^r
                if x>=48 and x<=90 and x>=97 and x<=123:
                    plainthird+=x
                else:
                    break
            for ad in listfour:
                for i in range(3,123,5):
                    s=ord(a[i])
                    x=ad^s
                    if x>=48 and x<=90 and x>=97 and x<=123:
                        plainfourth+=x
                    else:
                        break
                for ae in listfive:
                    for i in range(4,124,5):
                        t=ord(a[i])
                        x=ae^t
                        if x>=48 and x<=90 and x>=97 and x<=123:
                            plainfifth+=x
                        else:
                            break
