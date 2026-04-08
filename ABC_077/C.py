import bisect

n = int(input())
a = sorted(list(map(int, input().split())))
b = list(map(int, input().split()))
c = sorted(list(map(int, input().split())))

ans = 0

for mid in b:
	ap = bisect.bisect_left(a, mid)
	cp = bisect.bisect_right(c, mid)
	# print("d:", mid, ap * (n - cp))
	ans += ap * (n - cp)
print(ans)