n, m = map(int, input().split())

juices = [i for i in range(0, m + 1)]
for _ in range(n):
	l = int(input())
	drinks = list(map(int, input().split()))
	drink = 0
	for d in drinks:
		if juices[d] > 0:
			juices[d] = -1;
			drink = d
			break
	print(drink)