N, M, A, B = [int(l) for l in input().split()]
DP = [0] * N
DP[0] = True
LR = [0] * (N + 1)
for m in range(M):
    l, r = [int(l) - 1 for l in input().split()]
    LR[l] += 1
    LR[r + 1] += -1
num = 0
for i in range(N):
    num += LR[i]
    LR[i] = num
for i in range(N):
    if DP[i]:
        for j in range(A, B + 1):
            if i + j < N:
                if LR[i + j] == 0:
                    DP[i + j] = True
print("Yes" if DP[N - 1] else "No")
