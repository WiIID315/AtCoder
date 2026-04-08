x, y = input().split()
diff = ord(x) - ord(y)
if diff < 0:
	print('<')
elif diff > 0:
	print('>')
else:
	print('=')