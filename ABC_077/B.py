ans = 1
n = int(input())
for i in range(2, n):
	if i * i <= n:
		ans = i * i
	else:
		break
print(ans)