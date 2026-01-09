n, k = map(int, input().split())
x, y = [], []
points = []
for _ in range(n):
	a, b = map(int, input().split())
	points.append([a, b])
	x.append(a)
	y.append(b)

ans = 10000000000000000000

x.sort()
y.sort()

for i in range(n): #x start
	for j in range(n): #y start
		for m in range(i + 1, n): #x end
			for l in range(j + 1, n): #y end
				x_start = x[i]
				y_start = y[j]
				x_end = x[m]
				y_end = y[l]

				num_points = 0
				for a, b in points:
					if x_start <= a <= x_end and y_start <= b <= y_end:
						num_points += 1
				if num_points >= k:
					ans = min(ans, (x_end - x_start) * (y_end - y_start))

print(ans)