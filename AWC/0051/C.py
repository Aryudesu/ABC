N, M, K = map(int, input().split())
C = []
P = []
for n in range(N):
    c, p = map(int, input().split())
    C.append(c)
    P.append(p)
safe = [True] * (1 << N)
for m in range(M):
    u, v = map(int, input().split())
    b = (1 << (u-1)) | (1 << (v-1))
    for mask in range(1<<N):
        if mask & b == b:
            safe[mask] = False

result = 0
for mask in range(1 << N):
    if not safe[mask]:
        continue
    cost = 0
    val = 0
    for n in range(N):
        b = 1 << n
        if mask & b:
            cost += C[n]
            val += P[n]
    if cost > K:
        continue
    result = max(result, val)
print(result)
