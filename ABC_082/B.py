s, t = input(), input()

ss, sb = min(s), max(s)
ts, tb = min(t), max(t)

if(ss == sb == ts == tb):
	print("Yes" if len(s) < len(t) else "No")
else:
	print("Yes" if ss < tb else "No")