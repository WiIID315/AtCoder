n = int(input())
A = list(map(int, input().split()))
lengths = {}
ans = 0
for num in A:
	if num - 1 not in lengths:
		lengths.update({num: 1})
	else:
		lengths[num] = lengths[num - 1] + 1
	ans = max(ans, lengths[num])
# print(lengths)
print(ans)