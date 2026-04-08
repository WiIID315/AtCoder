a, b = input(), input()
print("YES" if a[0] == b[-1] and b[0] == a[-1] and a[1] == b[1] else "NO")