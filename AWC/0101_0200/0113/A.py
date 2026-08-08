N, M = map(int, input().split())
P = list(map(int, input().split()))
Q = list(map(int, input().split()))
result = []
for _ in range(M):
    K, *C = map(int, input().split())
    res = 0
    for c in C:
        res += P[c-1] - Q[c-1]
    result.append(res)
for res in result:
    print(res)
