N, M = map(int, input().split())
W = list(map(int, input().split()))
C = list(map(int, input().split()))
FULL = (1 << N) - 1
weight = [0] * (1 << N)
for i in range(N):
    b = 1 << i
    for j in range(1 << N):
        if (b & j) != 0:
            weight[j] += W[i]
ok = {0}
for i in range(M):
    capa = C[i]
    nextOK = ok.copy()
    for mask in ok:
        yet = FULL ^ mask
        nxt = yet
        while nxt:
            if weight[nxt] <= capa:
                nextOK.add(nxt | mask)
            nxt = (nxt - 1) & yet
    ok = nextOK
print("Yes" if FULL in ok else "No")
