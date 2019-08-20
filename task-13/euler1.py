n = int(input())
n1 = n - 1
v = ""
sum3 = 0
sum5 = 0

for i in range(0,n):
	
	num = int(input())
	
	times1 = int((num)/3) + 1
	times2 = int((num)/5) + 1
	
	for j in range (1,times1):
		
		sum3 = (3*j) + sum3
		print(sum3)
		
	for k in range (1,times2):
		
		sum5 = (5*k) + sum5
		print(sum5)

	sum = sum3 + sum5
	s = str(sum)
	v = v +" "+ s
	
v1 = list(map(str,v.split()))

for l in range(0,n1):
	
	v2 = v1[l]
	print(v2)
	
