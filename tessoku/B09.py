N = int(input())
# H, W = 5, 5
H, W = 1502, 1502
data = [[0] * (W + 2) for _ in range(H + 2)]
# (y, x)とする
# (b, a), (b, c)
# (d, a), (d, c)
for n in range(N):
    a, b, c, d = [int(l) for l in input().split()]
    data[b][a] += 1
    data[b][c] -= 1
    data[d][a] -= 1
    data[d][c] += 1
field1 = [[0] * (W + 2) for _ in range(H + 2)]
for h in range(H+2):
    s = 0
    for w in range(W+2):
        s += data[h][w]
        field1[h][w] = s
field2 = [[0] * (W + 2) for _ in range(H + 2)]
for w in range(W+2):
    s = 0
    for h in range(H+2):
        s += field1[h][w]
        field2[h][w] = s
result = 0
for h in range(H+2):
    for w in range(W+2):
        if field2[h][w] >= 1:
            result += 1
# for f in field2:
#     print(f)
print(result)
