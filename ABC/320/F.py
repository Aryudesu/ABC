N, H = [int(l) for l in input().split()]
TmpX = [int(l) for l in input().split()]
X = [0]
for t in TmpX:
    X.append(t)
PF = []
for n in range(N - 1):
    PF.append([int(l) for l in input().split()])
gasolin = []
for n in range(N):
    tmp = []
    tmp.append([False] * (H + 1))
    tmp.append([False] * (H + 1))
    gasolin.append(tmp)

gasolin[0][0][H] = True
for n in range(1, N + 1):
    dx = X[n] - X[n - 1]
    tg = gasolin[n-1][0][0]
    gasolin[n][0][0] = gasolin[n - 1]
