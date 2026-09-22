n = int(input())
a = [list(map(int, input().split())) for _ in range(2)]
dp = [[0] * n for _ in range(2)]

for i in range(2):
	for j in range(n):
		left = dp[i][j - 1] if j > 0 else 0
		right = dp[i - 1][j] if i > 0 else 0
		dp[i][j] = max(left, right) + a[i][j]
print(dp[1][n - 1])