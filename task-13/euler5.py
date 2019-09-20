#This script finds the LCM of all numbers present till n which is given as an input within some time constraints and trial input cases provided by hackerrank.

#The script first creates a list of numbers till n using (1) then it iterates through the list using (2)

# (1), a list is declared and using a for loop numbers are added till n

# (2), the script then iterates till the nth index term of the list and another loop (3) iterates through the elements in the list till the term the (2) for loop is at, to check if any numbers below n are its factors if they are factors the number is divided by that factor and stored back at that index in the list. This is to make sure that no factors are repeated.For example 6 will be divided by 1 first and 6 will be stored back, then 6/2 => 3 will be stored back instead of 6 at that place and similiarly 3/3=>1 hence 1 will replace 6 so that no factors are repeated. For 10 as input the final list would look like this:-
# [1, 2 , 3, 4=>2, 5, 6=>1, 7, 8=>2, 9=>3, 10=>1]

w=int(raw_input())
ans=[]
for p in range(1,w+1):
    n=int(input())
    f=1
    l=[]
    # (1)
    
    for a in range(1,n+1):
        l.append(a)
    # (2)
    
    for i in range(0,n):
        num=l[i]
        for j in range(0,i-1):
            probfact=l[j]
            if num%probfact==0:
                num=num/probfact
        l[i]=num
    for j in range(0,n):
        f=f*(l[j])
    ans.append(f)
for q in range(0,w):
    print ans[q]
