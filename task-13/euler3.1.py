a=int(raw_input())
m=[]
for w in range(1,a+1):
    n=int(raw_input())
    nn=n
    for i in range(1,n+1):
        if nn==1:
            break
        if n%i==0:
            factor=0
            for j in range(1,i+1):
                if nn==1:
                    break
                if i%j==0:
                    factor=factor+1
            if factor==2:
                pf=i
                nn=nn/i
    m.append(pf)
for x in range(0,a):
    print m[x]
