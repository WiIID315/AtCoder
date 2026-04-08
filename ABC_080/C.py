n = int(input())
shops = []
for _ in range(n):
	info = input().split()
	val = 0
	for open in info:
		val <<= 1
		if open == '1':
			val += 1
	shops.append(val)
scores = []
for _ in range(n):
	scores.append(list(map(int, input().split())))

ans = -1000000000

for i in range(1, 1024):
	temp_score = 0
	for j in range(n):

		temp_score += scores[j][(shops[j] & i).bit_count()]
	ans = max(temp_score, ans)
print(ans)