N, C = map(int, input().split())
times = [[0 for _ in range(200002)] for i in range(C + 1)]
shows = []

intensity = [0] * 200002
ans = 0

for _ in range(N):
	s, t, c = map(int, input().split())
	times[c][s * 2 - 1] += 1
	times[c][t * 2] -= 1

for channel in range(1, C + 1):
	for i in range(1, 200002):
		times[channel][i] += times[channel][i - 1]
		if times[channel][i]:
			intensity[i] += 1
		ans = max(ans, intensity[i])
print(ans)