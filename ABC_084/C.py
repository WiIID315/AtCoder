n = int(input())
stations = []
for _ in range(n - 1):
	stations.append(list(map(int, input().split())))

for i in range(n):
	time = 0
	for j in range(i, n - 1):
		c, s, f = stations[j]
		time = (max(time, s) + f - 1) // f * f
		time += c
	print(time)