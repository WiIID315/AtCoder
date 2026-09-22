n = int(input())
time = 0
curr_x = 0
curr_y = 0
valid = True

for _ in range(n):
	if not valid:
		break
	t, x, y = map(int, input().split())
	dist = abs(curr_x - x) + abs(curr_y - y)
	if(dist > (t - time) or (dist & 1) ^ ((t - time) & 1)):
		valid = False
	time = t
	curr_x = x
	curr_y = y
print("Yes" if valid else "No")