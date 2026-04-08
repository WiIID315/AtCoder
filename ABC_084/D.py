q = int(input())
qs = []
up = 0
for _ in range(q):
	l, r = map(int, input().split())
	up = max(r, up)
	qs.append([l, r])

lp = [0] * (up + 1)
prefix = [0] * (up + 1)
pr = []

for i in range(2, up + 1):
	if lp[i] == 0:
		lp[i] = i
		pr.append(i)
	j = 0
	while i * pr[j] <= up:
		lp[i * pr[j]] = pr[j]
		if pr[j] == lp[i]:
			break
		j += 1

check = set(pr)
for i in range(1, up + 1):
	prefix[i] = prefix[i - 1]
	if i % 2 and i in check and (i + 1) // 2 in check:
		prefix[i] += 1

for l, r in qs:
	print(prefix[r] - prefix[l - 1])