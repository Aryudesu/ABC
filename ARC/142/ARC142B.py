def makeField(N):
    res = []
    for n in range(N):
        tmp = []
        for m in range(N):
            tmp.append(1 + m + n * N)
        res.append(tmp)
    return res


N = int(input())
res = makeField(N)
for i in range(N):
    if i % 2 == 1:
        for j in range(N//2):
            res[i][j*2 + 1], res[i][j*2] = res[i][j*2], res[i][j*2 + 1]
    else:
        for j in range(N//2):
            if j*2 + 2 < N:
                res[i][j*2 + 2], res[i][j*2 + 1] = res[i][j*2 + 1], res[i][j*2 + 2]

for r in res:
    print(' '.join(map(str,r)))
