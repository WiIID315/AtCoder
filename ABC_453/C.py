n = int(input())
a = list(map(int, input().split()))
ans = 0

p = [(0.5, 0)]
for dist in a:
	new_list = []
	for pos, count in p:
		new_list.append((pos - dist, count + 1 if (pos) * (pos - dist) < 0 else count))
		ans = max(ans, new_list[-1][1])
		new_list.append((pos + dist, count + 1 if (pos) * (pos + dist) < 0 else count))
		ans = max(ans, new_list[-1][1])
	p = new_list
print(ans)