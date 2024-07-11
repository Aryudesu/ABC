N, K = [int(l) for l in input().split()]
P = []
result = [False] * N
for n in range(N):
    P.append((sum([int(l) for l in input().split()]), n))
P.sort(reverse=True)
T = P[K - 1][0]
for n in range(N):
    p, q = P[n]
    result[q] = p + 300 >= T
for r in result:
    print("Yes" if r else "No")
