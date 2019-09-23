import hashlib
from ctypes import CDLL

a="05181c2638270301601329023a203c2324072229230401273f2a1b0b02252b071e243e2313262923352411332336031b2f2d27191602383f07062e0827041725092e161e2d2f281017092f34123b321e2e12342d2b210c0b0e3f191f33370f1935000e2123392d132f163213152308302d0a0f3f282a0e183b"
a=a.decode("hex")
o=0
for aa in range(65,91) + range(97, 123):
    if o==1:
        break
    plainfirst=""
    for i in range(0,125,5):
        p=ord(a[i])
        x=aa^p
        if x>=48 and x<=90 and x>=97 and x<=123:
            plainfirst+=ord(x)
        else:
            break
    for ab in range(65,91) + range(97, 123):
        if o==1:
            break
        plainsecond=""
        for i in range(1,121,5):
            q=ord(a[i])
            x=ab^q
            if x>=48 and x<=90 and x>=97 and x<=123:
                plainsecond+=ord(x)
            else:
                break    
        for ac in range(65,91) + range(97, 123):
            if o==1:
                break
            plainthird=""
            for i in range(2,122,5):
                r=ord(a[i])
                x=ac^r
                if x>=48 and x<=90 and x>=97 and x<=123:
                    plainthird+=ord(x)
                else:
                    break
            for ad in range(65,91) + range(97, 123):
                if o==1:
                    break
                plainfourth=""
                for i in range(3,123,5):
                    s=ord(a[i])
                    x=ad^s
                    if x>=48 and x<=90 and x>=97 and x<=123:
                        plainfourth+=ord(x)
                    else:
                        break
                for ae in range(65,91) + range(97, 123):
                    if o==1:
                        break
                    plainfifth=""
                    for i in range(4,124,5):
                        t=ord(a[i])
                        x=ae^t
                        if x>=48 and x<=90 and x>=97 and x<=123:
                            plainfifth+=ord(x)
                        else:
                            break
                        plaintext=""
                        p=chr(aa)
                        q=chr(ab)
                        r=chr(ac)
                        s=chr(ad)
                        t=chr(ae)
                        k=p+q+r+s+t
                        print k
                        for zz in range(0,24):
                            plaintext+=plainfirst[zz]+plainsecond[zz]+plainthird[zz]+plainfourth[zz]+plainfifth[zz]
                        
                        plaintext=plaintext+plainfirst[24]
                        flag="{"+plaintext+"}"
                        if hashlib.md5(flag).digest().encode("hex") == "d444d1ac3799a86d31f34b4a8a3243c6":
                            o=1
                            ans=flag
                            kk=k                            
print "----------------"
print ans
print "##########"
print kk
