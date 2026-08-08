N, M, Q = map(int, input().split())
data = [None] * N
for m in range(M):
    p, c = input().split()
    data[int(p)-1] = c
# print(data)
result = []
for _ in range(Q):
    T = input()
    isOk = True
    for idx in range(N):
        t = T[idx]
        if data[idx] is None:
            continue
        if data[idx] != t:
            isOk = False
    result.append("Yes" if isOk else "No")
for r in result:
    print(r)
