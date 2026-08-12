N, Q = map(int, input().split())
data = []
sm = 0
for n in range(N):
    p, d = map(int, input().split())
    data.append(p - sm)
    sm += d
query = []
for _ in range(Q):
    s = int(input())
    query.append(s)
sortedQuery = sorted(set(query))
idx = 0
resData = dict()
while sortedQuery:
    q = sortedQuery.pop()
    while idx < N:
        if q <= data[idx]:
            idx += 1
        else:
            break
    resData[q] = idx
result = []
for q in query:
    result.append(resData[q])
print(*result, sep="\n")
