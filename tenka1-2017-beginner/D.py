n, k = map(int, input().split())
masks = [k]
for r in range(31):
	if (1 << r) > k:
		break 
	if (k >> r) & 1:
		masks.append(((k >> r) << r) - 1)
# print(masks)

ans = 0
options = []
for _ in range(n):
	options.append(list(map(int, input().split())))

for mask in masks:
	temp = 0
	for option in options:
		if option[0] & mask == option[0]:
			temp += option[1]
	ans = max(ans, temp)
print(ans)