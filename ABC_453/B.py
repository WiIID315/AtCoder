t, x = map(int, input().split())
prev = -x

times = list(map(int, input().split()))
for i in range(t + 1):
	if abs(prev - times[i]) >= x:
		print(i, times[i])
		prev = times[i]