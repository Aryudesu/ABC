N, K = map(int, input().split())
C = []
for n in range(N):
    C.append(list(map(int, input().split())))
MAX_POW = 32
data = []
for n in range(N):
    dat = []
    for i in range(N):
        dat.append(C[n][i])
    data.append(dat)
    for num in range(MAX_POW):
        dat = data[num]
        nextData = [0] * N
        for i in range(N):
            for j in range(N):
                C[i][j]

