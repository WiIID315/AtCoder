from math import comb
n, d = map(int, input().split())
enters = [0] * (10**6 + 2)
for _ in range(n):
	s, t = map(int, input().split())
	enters[s] += 1
	enters[t] -= 1

prefix = [0] * (10**6 + 1)
for i in range(10**6 + 1):
	prefix[i] = prefix[i - 1]
	prefix[i] += enters[i]
combos = 0
left = 1
right = 1
while left <= 10**6:
	right = left
	if(prefix[left] < 2):
		left += 1
		continue
	while(right <= 10**6 and prefix[right] >= 2):
		if right - left + 1 >= d:
			print(left, right, prefix[left], prefix[right])
			combos += comb(min(prefix[left], prefix[right]), 2)
			left += 1
		right += 1
	else:
		left = right
	left += 1
print(combos)