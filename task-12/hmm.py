import string

a=raw_input()
b=a.decode("hex")

print b

l=len(b)
m=[]
for i in range(0,l):
    x=b[i]
    c=chr(ord(x)^10)
    m.append(c)
print m

x=m
upper = string.ascii_uppercase
lower = string.ascii_lowercase
digits = string.digits
n = []
for i in x:
    if i.isupper() is True:
        n.append(upper[(upper.index(i)-3)%26])
    elif i.islower() is True:
        n.append(lower[(lower.index(i)-3)%26])
    elif i.isdigit() is True:
        n.append(digits[(digits.index(i)-3)%10])
print n
