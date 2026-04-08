abcd = input()
a = int(abcd[0])
b = int(abcd[1])
c = int(abcd[2])
d = int(abcd[3])

if (a + b + c + d == 7):
	print((abcd[0] + "+" + abcd[1] + "+" + abcd[2] + "+" + abcd[3] + "=7"))
elif a + b + c - d == 7:
	print((abcd[0] + "+" + abcd[1] + "+" + abcd[2] + "-" + abcd[3] + "=7"))
elif a + b - c + d == 7:
	print((abcd[0] + "+" + abcd[1] + "-" + abcd[2] + "+" + abcd[3] + "=7"))
elif a + b - c - d == 7:
	print((abcd[0] + "+" + abcd[1] + "-" + abcd[2] + "-" + abcd[3] + "=7"))
elif a - b + c + d == 7:
	print((abcd[0] + "-" + abcd[1] + "+" + abcd[2] + "+" + abcd[3] + "=7"))
elif a - b + c - d == 7:
	print((abcd[0] + "-" + abcd[1] + "+" + abcd[2] + "-" + abcd[3] + "=7"))
elif a - b - c + d == 7:
	print((abcd[0] + "-" + abcd[1] + "-" + abcd[2] + "+" + abcd[3] + "=7"))
elif a - b - c - d == 7:
	print((abcd[0] + "-" + abcd[1] + "-" + abcd[2] + "-" + abcd[3] + "=7"))