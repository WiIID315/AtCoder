t = int(input())

for tt in range(t):
	n, d = map(int, input().split())
	A = list(map(int, input().split()))
	B = list(map(int, input().split()))

	# print(n, d, A, B)

	eggs = [0] * (n + 1)
	ptr = 0
	for day in range(n):
		eggs[day] += A[day]
		rem = B[day]
		while rem > 0:
			# print(rem, eggs)
			temp = min(rem, eggs[ptr])
			rem -= min(eggs[ptr], temp)
			eggs[ptr] -= min(eggs[ptr], temp)
			if eggs[ptr] == 0:
				ptr += 1
		if day - ptr >= d:
			ptr += 1

	ans = 0
	while ptr <= n:
		ans += eggs[ptr]
		ptr += 1
	print(ans)
