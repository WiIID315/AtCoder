from collections import Counter

n, k = map(int, input().split())
a = Counter(map(int, input().split()))
size = len(a)
nums = list(a.keys())
nums.sort(key= lambda x: a[x])
count = 0
for val in nums[:size - k]:
	count += a[val]
print(count)