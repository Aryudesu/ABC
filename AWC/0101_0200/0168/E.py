N, M = map(int, input().split())
A = list(map(int, input().split()))
INF = 10 ** 18
result = 0
ngs = [0] * (1 << N)
for m in range(M):
    p, c, *X = map(int, input().split())
    b = 0
    for x in X:
        b |= 1 << (x-1)
    ngs[b] |= 1 << (p-1)

for mask in range(1 << N):
    for n in range(N):
        b = mask | (1 << n)
        ngs[b] |= ngs[mask]

result = [-INF] * (1 << N)
result[0] = 0
goal = (1 << N) - 1
for mask in range(1 << N):
    remain = goal ^ mask
    while remain:
        p = remain.bit_length() - 1
        b = 1 << p
        remain ^= b
        if ngs[mask] & b:
            continue
        nextMask = mask | b
        result[nextMask] = max(A[p] + result[mask], result[nextMask])
print(max(result))
