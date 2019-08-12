import pytesseract
from PIL import Image 

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
v = str(pytesseract.image_to_string(Image.open('F:\Beginner\pic\div.png')))
arr = list(map(str,v.split()))

f = int(arr[0])
m = arr[1]
l = int(arr[2])

add = "+"
sub = "-"
mul = "*"
div = "/"

if m == add:
	
	result = f + l
	
elif m == sub:
	
	result = f - l

elif m == mul:
	
	result = f * l

elif m == div:
	
	result = f / l
else:
	
	result = "Operand not recognised"

print (result)
