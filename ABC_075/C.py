# I forget Tarjan's I had to look it up -.-
n, m = map(int, input().split())
adj = [[] for _ in range(n)]
for _ in range(m):
	a, b = map(int, input().split())
	a -= 1
	b -= 1
	adj[a].append(b)
	adj[b].append(a)

time = 0
visited = [False] * n
time_in = [-1] * n
low = [-1] * n

bridges = 0

def dfs(v, p = -1):
	global time, bridges, time_in, visited, low
	visited[v] = True
	time_in[v] = low[v] = time
	skipped_parent = False
	time += 1

	for u in adj[v]:
		if u == p and not skipped_parent:
			skipped_parent = True
			continue
		if visited[u]:
			low[v] = min(low[v], time_in[u])
		else:
			dfs(u, v)
			low[v] = min(low[v], low[u])
			if low[u] > time_in[v]:
				bridges += 1

dfs(0)

print(bridges)