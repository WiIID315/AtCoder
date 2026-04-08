n = int(input())
a = list(map(int, input().split()))

h, idx = 0, -1

for i in range(n):
	if abs(a[i]) > h:
		h = abs(a[i])
		idx = i

steps = []

if a[idx] < 0:
	for i in range(n):
		if(a[i] > 0):
			steps.append([idx + 1, i + 1])
			a[i] += a[idx]
	for i in range(n - 1, 0, -1):
		steps.append([i + 1, i])
elif a[idx] > 0:
	for i in range(n):
		if(a[i] < 0):
			steps.append([idx + 1, i + 1])
			a[i] += a[idx]
	for i in range(n - 1):
		steps.append([i + 1, i + 2])

print(len(steps))
for step in steps:
	print(*step)