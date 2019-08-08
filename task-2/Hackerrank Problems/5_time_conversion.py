arr = input()
arr1 = list(map(str,arr.split(':')))
c = int(arr1[0]) + 12
m = arr[8:]
n = "PM"

x = arr[0:2]
x1 = "12"

if x == x1:

	if m == n:
		
		p = "12"
		q = arr[2:8]
		d = p + q
		print (d)
	
	else:
		
		p = "00"
		q = arr[2:8]
		d = p + q
		print (d)

elif m == n:
	
	c1 = str(c)
	c2 = arr[6:8]
	d = c1 + ":" + arr1[1] + ":"  + c2
	print (d)

else:
	
	e = arr[0:8]
	print(e)
