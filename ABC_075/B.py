h, w = map(int, input().split())
strs = []
for _ in range(h):
	strs.append(input())

r = [-1 , -1, -1, 0, 1, 1, 1, 0]
c = [-1, 0, 1, 1, 1, 0, -1, -1]

for i in range(h):
	row = ''
	for j in range(w):
		if strs[i][j] == '#':
			row += '#'
			continue
		count = 0
		for k in range(8):
			if 0 <= i + r[k] < h and 0 <= j + c[k] < w and strs[i + r[k]][j + c[k]] == '#':
				count += 1
		row += str(count)
	print(row)