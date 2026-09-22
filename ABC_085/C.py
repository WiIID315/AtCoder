n, y = map(int, input().split())

def find():
	for a in range(n + 1):
		for b in range(n + 1 - a):
			c = n - a - b
			total = a * 10000 + b * 5000 + c * 1000
			if total == y:
				print(a, b, c)
				return
	print(-1, -1, -1)
find()