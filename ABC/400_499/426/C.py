from heapq import heappop, heappush

N, Q = [int(l) for l in input().split()]
data = {i: 1 for i in range(N)}
sData = []
for i in range(N):
    heappush(sData, i)
result = []
for q in range(Q):
    x, y = [int(l) - 1 for l in input().split()]
    tmp = 0
    while True:
        s = heappop(sData)
        if s > x:
            heappush(sData, s)
            break
        tmp += data[s]
        data[s] = 0
    result.append(tmp)
    data[y] += tmp
for r in result:
    print(r)
