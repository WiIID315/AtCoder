import sys
sys.setrecursionlimit(2000)

h, w = map(int, input().split())
mat = []
start = ()
for i in range(h):
	s = input()
	if s.find('S') != -1:
		start = (i, s.find('S'))
	mat.append(s)

dp = [[[0 for i in range(4)] for j in range(w)] for k in range(h)]
dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
letters = ['U', 'D', 'L', 'R']
found = False

def dfs(r, c, dir, path):
	global found
	if(found or r < 0 or r >= h or c < 0 or c >= w or mat[r][c] == '#' or dp[r][c][dir]):
		return
	if(mat[r][c] == 'G'):
		print('Yes')
		print(path)
		found = True
		return
	dp[r][c][dir] = True
	if(mat[r][c] == 'o'):
		dfs(r + dirs[dir][0], c + dirs[dir][1], dir, path + letters[dir])
	elif(mat[r][c] == 'x'):
		for i in range(4):
			if i != dir:
				dfs(r + dirs[i][0], c + dirs[i][1], i, path + letters[i])
	else:
		for i in range(4):
			dfs(r + dirs[i][0], c + dirs[i][1], i, path + letters[i])
dfs(start[0], start[1], 0, '')

if not found:
	print("No")
