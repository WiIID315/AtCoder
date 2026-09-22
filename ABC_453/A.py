n = int(input())
s = input()
o = True

ans = ''
for c in s:
	if o and c == 'o':
		continue
	if c != 'o':
		o = False
	ans += c
print(ans)