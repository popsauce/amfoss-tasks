n=int(input())
l=[]
u=0
for i in range(1,n+1):
    num=int(input())
    a=int(num/2)+1
    for j in range(1,a+1) + range(num,num+1):
        factor=0
        b=int(j/2)+1
        for k in range(1,b+1) + range(j,j+1):
            rem=j%k
            if rem==0:
                factor=factor+1
        if factor==2 and num%j==0:
            f=j
    l.append(f)

    
for m in range(0,n):
    print(l[m])
