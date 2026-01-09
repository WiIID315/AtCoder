n = int(input())
if(n % 2 == 0):
	print(n // 2, n, n)
else:
	b = False
	for i in range(1, 3501):
		if b:
			break
		for j in range(1, 3501):
			if b:
				break
			bottom = n * i * j;
			top = 4 * i * j - n * j - n * i
			if top > 0 and bottom % top == 0:
				print(i, j, bottom // top)
				b = True