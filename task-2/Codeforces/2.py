n = int(input())
n1 = n - 1
final = ""

for i in range(0,n):
	
	s = str(input())
	a = s[0]
	b = len(s)
	b1 = b - 1
	a1 = s[b1]
	c = b - 2
	
	if b > 10:
		
		beg = str(a)
		mid = str(c)
		end = str(a1)
		cut = " "
	
		final = final + beg + mid + end + cut 
	
	else:
		
		cut = " "
		final = final + s + cut
		
for j in range (0,n):
	
	arr = list(map(str,final.split()))
	out = arr[j]
	print(out)
