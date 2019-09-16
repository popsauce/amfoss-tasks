n=int(input())
z=[]
for i in range(1,n+1):
    num=int(input())
    n=0
    while n!=1:
        a=str(num)
        b=num
        if a[0]==a[5] and a[1]==a[4] and a[2]==a[3]:
            for j in range(999,99,-1):
                rem=b%j
                if rem==0:
                    l=len(str(b/j))
                    if l==3: 
                        ans=j
                        n=1
        else:
            p=int(a[0]+a[1]+a[2])-1
            q=str(p)
            num=int(q[0]+q[1]+q[2]+q[2]+q[1]+q[0])
    z.append(ans)
for i in range(0,n):
    print(z[i])
