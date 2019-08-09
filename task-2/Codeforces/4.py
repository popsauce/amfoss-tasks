n = int(input())
result = 0


for i in range(0,n):

	s = str(input())
	add = "++x"
	sub = "x--"
	
	if s == add:
		
		result = result + 1
		
	else:
		
		result = result - 1
		
print (result)
