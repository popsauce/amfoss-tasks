//Some cases are not displaying proper output

n = input()
arr = list(map(int,n.split()))
values = int(arr[0])
cutoff = int(arr[1])
marks = input()
ind = list(map(int,marks.split()))
a = 0
k = ind[a]
passed = 0

while k >= cutoff:
	
	if a <= values:
		
		k = ind[a]
		a = a + 1
		passed = passed + 1
		
print(passed)
