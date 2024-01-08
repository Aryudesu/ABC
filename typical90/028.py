field = []
H, W = 1001, 1001
for i in range(H):
    field.append([0 for _ in range(W)])
N = int(input())
for n in range(N):
    lx, ly, rx, ry = [int(l) for l in input().split()]
    field[ly][lx] += 1
    field[ry][rx] += 1
    field[ly][rx] -= 1
    field[ry][lx] -= 1

for i in range(H):
    s = 0
    for j in range(W):
        s += field[i][j]
        field[i][j] = s

for i in range(W):
    s = 0
    for j in range(H):
        s += field[j][i]
        field[j][i] = s

result = dict()
for i in range(W):
    for j in range(H):
        if field[j][i]:
            result[field[j][i]] = result.get(field[j][i], 0) + 1

for i in range(1, N + 1):
    print(result.get(i, 0))
