n = int(input())
mochis = []
for _ in range(n):
	mochis.append(int(input()))
mochis.sort(reverse=True)
count = 1
prev = mochis[0]

for i in range(1, n):
	if(mochis[i] < prev):
		count += 1
		prev = mochis[i]
print(count)