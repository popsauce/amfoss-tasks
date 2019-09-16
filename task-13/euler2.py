n=int(input())
l=[]

for i in range(1,n+1):
    s=0
    a=1
    b=1
    t=2
    num=int(input())
    while a<=num and b<=num:
        t=t+1
        a=a+b
        if a>num:
            break
        if t%3==0:
            s=s+a
        
        t=t+1
        b=b+a
        if b>num:
            break
        if t%3==0:
            s=s+b
    l.append(s)
for j in range(0,n):
    print(l[j])
