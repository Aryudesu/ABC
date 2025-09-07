N, M = [int(l) for l in input().split()]
S = []
result = [0] * N
for n in range(N):
    S.append(input())
for m in range(M):
    z = 0
    o = 0
    for n in range(N):
        if S[n][m] == "0":
            z += 1
        else:
            o += 1
    for n in range(N):
        if z == 0 or o == 0:
            result[n] += 1
        elif z < o:
            if S[n][m] == "0":
                result[n] += 1
        elif z > o:
            if S[n][m] == "1":
                result[n] += 1
MA = max(result)
res = []
for n in range(N):
    if result[n] == MA:
        res.append(n + 1)
print(*res)
