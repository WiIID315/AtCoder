n = int(input())
k = int(input())
start = 1
for _ in range(n):
	if start * 2 < start + k:
		start *= 2
	else:
		start += k
print(start)