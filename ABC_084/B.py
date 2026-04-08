a, b = map(int, input().split())
code = input().split('-')
valid = True
z = ord('0')

if len(code) != 2 or len(code[0]) != a or len(code[1]) != b:
	valid = False
else:
	for c in code[0]:
		if not 0 <= ord(c) - z <= 9:
			valid = False
	for c in code[1]:
		if not 0 <= ord(c) - z <= 9:
			valid = False
print("Yes" if valid else "No")