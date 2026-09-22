n, h = map(int, input().split())
a, b = [0] * n, [0] * n
for i in range(n):
	a[i], b[i] = map(int, input().split())
high = max(a)
throws = sorted([throw for throw in b if throw > high], reverse=True)
ans = (h + high - 1) // high
for i in range(len(throws)):
	if(h < 0): 
		break
	ans = min(ans, i + 1 + max(0, (h - throws[i] + high - 1) // high))
	h -= throws[i]
print(ans)