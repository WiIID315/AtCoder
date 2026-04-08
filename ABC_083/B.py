n, a, b = map(int, input().split())

def count(num):
	sum = 0
	while num > 0:
		sum += num % 10
		num //= 10
	return sum

ans = 0
for i in range(1, n + 1):
	if(a <= count(i) <= b):
		ans += i
print(ans)