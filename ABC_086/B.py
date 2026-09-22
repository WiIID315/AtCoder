import math
a, b = input().split()
concat = int(a + b)
if int(math.sqrt(concat)) == math.sqrt(concat):
	print("Yes")
else:
	print("No")