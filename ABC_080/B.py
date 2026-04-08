n = input()
harshad = 0
for c in n:
	harshad += int(c)
print("Yes" if int(n) % harshad == 0 else "No")