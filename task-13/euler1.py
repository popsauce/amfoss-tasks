n=int(input())
l=[]
for i in range(1,n+1):
    num=int(input())-1
    t=int(num/3)
    f=int(num/5)
    ft=int(num/15)

    st=1.5*t*(t+1)
    sf=2.5*f*(f+1)
    sft=7.5*ft*(ft+1)

    sum=int(st+sf-sft)
    l.append(sum)

for j in range(0,n):
    print(l[j])	
