n = int(input())

nums = [[] for _ in range(10)]
for k in range(1, 10):
	l = (10 ** (k - 1) - 1).bit_length()
	r = (10 ** k - 1).bit_length()
	nums[k] = [1 << i for i in range(l, r)]

ans = []
build = [set() for _ in range(10)]
build[0] = {0}

for k in range(1, 10):
	for i in range(1, k + 1):
		build[k] |= {x * (10 ** i) + p for x in build[k - i] for p in nums[i]}
	ans += list(build[k])
ans.sort()
print(ans[n - 1])