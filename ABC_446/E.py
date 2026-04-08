m, a, b = map(int, input().split())
pairs = 0
seen = [set() for _ in range(m)]
for x in range(1, m):
	for y in range(1, m):
		s1, s2 = x, y
		while s1 % m != 0:
			new_val = (s1 * a + s2 * b) % m
			if new_val in seen[s1]:
				break
			if new_val != 0:
				seen[s2].add(s1)
			s2 = s1
			s1 = new_val
		if s1 % m != 0:
			pairs += 1

print(pairs)
