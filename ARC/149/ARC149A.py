N, M = [int(l) for l in input().split()]
DP = [0, 0, 0, 0, 0, 0, 0, 0, 0]
resN = -1
resD = 1
for n in range(1, N + 1):
    for i in range(9):
        DP[i] = (DP[i] * 10 + (i+1)) % M
        if DP[i] == 0:
            resN = n
            resD = i + 1
if resN == -1:
    print(-1)
else:
    print(str(resD) * resN)
