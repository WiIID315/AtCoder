S = input()
T = input()
start_pos = -1

for i in range(len(S) - len(T) + 1):
	valid = True
	for j in range(len(T)):
		if not (S[i + j] == T[j] or S[i + j] == '?'):
			valid = False
			break
	if valid:
		start_pos = i
if start_pos == -1:
	print('UNRESTORABLE')
else:
	ans = ''
	for i in range(len(S)):
		if start_pos <= i < start_pos + len(T):
			ans += T[i - start_pos]
		elif S[i] == '?':
			ans += 'a'
		else:
			ans += S[i]
	print(ans)
