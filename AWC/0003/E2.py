N, M = map(int, input().split())
W = list(map(int, input().split()))
C = list(map(int, input().split()))
C.sort(reverse=True)
FULL = (1 << N) - 1

weight = [0] * (1 << N)
for i in range(N):
    bit = 1 << i
    for j in range(1 << N):
        if (j & bit) != 0:
            weight[j] += W[i]

data = [False] * (1 << N)
data[0] = True
for i in range(M):
    nextData = data.copy()
    for mask in range(1 << N):
        if not data[mask]:
            continue
        if mask == FULL:
            continue

        yet = FULL ^ mask
        sub = yet
        while sub:
            if weight[sub] <= C[i]:
                newMask = mask | sub
                if not nextData[newMask]:
                    nextData[newMask] = True
            sub = (sub - 1) & yet
    data = nextData
    if data[FULL]:
        break

print("Yes" if data[FULL] else "No")
