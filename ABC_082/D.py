s = input()
x, y = map(int, input().split())

forward_x = s.find('T')
i = forward_x if forward_x != -1 else len(s)
y_aligned = True

offset = len(s)
x_dp = [False] * (2 * offset + 1)
y_dp = [False] * (2 * offset + 1)
x_dp[offset + i], y_dp[offset] = True, True

xs = []
ys = []

while i != -1:
	next_t = s.find('T', i + 1)
	dist = next_t - i - 1 if next_t != -1 else len(s) - i - 1
	if(dist == -1):
		break
	elif dist == 0:
		y_aligned = not y_aligned
		i += 1
		continue
	if y_aligned:
		ys.append(dist)
	else:
		xs.append(dist)
	y_aligned = not y_aligned
	i = next_t

# print(xs)
# print(ys)


for fuck in xs:
	new_dp = [False] * (2 * offset + 1)
	for i in range(2 * offset + 1):
		if x_dp[i]:
			if i - fuck >= 0:
				new_dp[i - fuck] = True
			if i + fuck < 2 * offset + 1:
				new_dp[i + fuck] = True
	x_dp = new_dp

for poo in ys:
	new_dp = [False] * (2 * offset + 1)
	for i in range(2 * offset + 1):
		if y_dp[i]:
			if i - poo >= 0:
				new_dp[i - poo] = True
			if i + poo < 2 * offset + 1:
				new_dp[i + poo] = True
	y_dp = new_dp

print("Yes" if y_dp[y + offset] and x_dp[x + offset] else "No")