S = input()
n = len(S)
k = n

for i in range(n - 1):
	if S[i] != S[i + 1]:
		k = min(k, max(i + 1, n - i - 1))
print(k)