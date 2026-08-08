N, M = map(int, input().split())
W = list(map(int, input().split()))
result = []
for m in range(M):
    k, *A = map(int, input().split())
    res = 0
    for a in A:
        res += W[a-1]
    result.append(res)
for r in result:
    print(r)
