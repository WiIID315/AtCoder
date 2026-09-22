n = int(input())
points = []
for _ in range(n):
	x, y = map(int, input().split())
	points.append([x, y])
points.sort(key=lambda x: (x[0], x[1]))
smallest = n
count = 0
for x, y in points:
	if y <= smallest:
		count += 1
		smallest = y
print(count)