from collections import Counter

n = int(input())
a = Counter(map(int, input().split()))
count = 0
for k, v in a.items():
	if k != v:
		if v > k:
			count += v - k
		else:
			count += v
print(count)