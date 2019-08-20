//Facing some errors

n = str(input())
l = len(n) - 2
k = 0
y = "YES"
n = "NO"

for i in range(0,l):
	
	a = n[i]
	b = i + 1
	
	c = n[b]
	
	if a == c:
		
		k = k + 1
		
		if k >= 6:
			
			v = "YES"
			
			
		else:
			k = 0
if v == y:
	print (y)
else:
	print(n)
