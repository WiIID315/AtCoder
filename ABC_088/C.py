mat = []
for _ in range(3):
	mat.append(list(map(int, input().split())))

adiff = mat[1][0] - mat[0][0] == mat[1][1] - mat[0][1] == mat[1][2] - mat[0][2]
bdiff = mat[2][0] - mat[0][0] == mat[2][1] - mat[0][1] == mat[2][2] - mat[0][2]
print("Yes" if adiff and bdiff else "No")