n = int(input())
higha, highb = 0, 0
for _ in range(n):
	a, b = map(int, input().split())
	if a > higha:
		higha, highb = a, b
print(higha + highb)