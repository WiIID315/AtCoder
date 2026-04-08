n = int(input())
nums = list(map(int, input().split()))

ans = 10 ** 9
for n in nums:
	count = 0
	while not n % 2:
		count += 1
		n >>= 1
	ans = min(ans, count)
print(ans)