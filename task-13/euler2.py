n = int(input())
n1 = int(n/2)
a=0
b=1
sum = 0
sums=0

while a<=n & b<=n:
	
	a = a+b
	print(a)
	include= a%2
	
	if include == 0:
		
		sum = a + sum
	
	sums = a + sums
	if a > n:
		break
	b = a+b
	print(b)
	include1= b%2
	
	if include1 == 0:
		
		sum = b + sum
		
	sums = b + sums


print(sum)
