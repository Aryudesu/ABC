N = int(input())
Field = []
for i in range(100):
    tmp = []
    for j in range(100):
        tmp.append(False)
    Field.append(tmp)
for n in range(N):
    A, B, C, D = [int(l) for l in input().split()]
    for i in range(B - A):
        for j in range(D - C):
            Field[A + i][C + j] = True
result = 0
for i in range(100):
    for j in range(100):
        if Field[i][j]:
            result += 1
# for f in Field:
#     print(f)
print(result)
