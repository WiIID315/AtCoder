import heapq

Q = int(input())
heap = []
for _ in range(Q):
	a, b = map(int, input().split())
	if(a == 1):
		heapq.heappush(heap, b)
	else:
		while(heap and heap[0] <= b):
			heapq.heappop(heap);
	print(len(heap))