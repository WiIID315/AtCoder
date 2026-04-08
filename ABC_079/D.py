h, w = map(int, input().split())

adj = []

for i in range(10):
	adj.append(list(map(int, input().split())))

for k in range(10):
	for i in range(10):
		for j in range(10):
			if(adj[i][k] + adj[k][j] < adj[i][j]):
				adj[i][j] = adj[i][k] + adj[k][j]

ans = 0

for i in range(h):
	row = list(map(int, input().split()))
	for val in row:
		if(val != -1):
			ans += adj[val][1]
print(ans)