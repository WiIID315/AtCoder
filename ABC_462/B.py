n = int(input())
ans = [[] for _ in range(n + 1)]
for i in range(n):
	var = list(map(int, input().split()))
	for j in range(1, var[0] + 1):
		ans[var[j]].append(i + 1)
for row in ans[1:]:
	print(len(row), *row)