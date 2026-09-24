from collections import deque

n, m = map(int, input().split())
visited = [[float('inf')] * m for _ in range(n)]
visited[0][0] = 1
num_whites = 0
maze = []
for _ in range(n):
	maze.append(input())
	for c in maze[-1]:
		if c == '.':
			num_whites += 1

q = deque()
q.append((0, 0))
dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]
while q:
	size = len(q)
	for _ in range(size):
		r, c = q.popleft()
		if maze[r][c] == '#':
			continue

		dist = visited[r][c]
		for dir in dirs:
			if 0 <= r + dir[0] < n and 0 <= c + dir[1] < m and visited[r + dir[0]][c + dir[1]] > dist + 1:
				visited[r + dir[0]][c + dir[1]] = dist + 1
				q.append((r + dir[0], c + dir[1]))





if visited[n - 1][m - 1] == float('inf'):
	print(-1)
else:
	print(num_whites - visited[n - 1][m - 1])