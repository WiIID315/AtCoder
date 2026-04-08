n = int(input())
adj = [[] for _ in range(n)]
for i in range(n):
	adj[i] = [0] * (i + 1) + list(map(int, input().split()))
print(adj)

accounted_for = [False] * n
accounted_for[0] = True

for i in range(1, n):
	for j in range(1, i):
		# print(adj[0][i], adj[i][j], adj[0][j])
		if i != j and adj[0][i] == adj[0][j] + adj[j][i]:
			if(i == 3):
				print("huh", j)
			accounted_for[i] = True
print(accounted_for)
print("Yes" if False not in accounted_for else "No")