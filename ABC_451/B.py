n, m = map(int, input().split())
ans = [0] * m
for _ in range(n):
	a, b = map(int, input().split())
	ans[a - 1] -= 1
	ans[b - 1] += 1

for val in ans:
	print(val)