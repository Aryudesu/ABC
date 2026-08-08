from heapq import heappop, heappush

N, M = map(int, input().split())
HS = []
for n in range(N):
    h, s = map(int, input().split())
    HS.append((h, s))
HS.sort(reverse=True)
P = list(map(int, input().split()))
P.sort()
count = 0
result = 0
data = []
for p in P:
    while HS:
        h, s = HS.pop()
        if h > p:
            HS.append((h, s))
            break
        heappush(data, -s)
    if data:
        s = -heappop(data)
        result += s
        count += 1
if count != M:
    print(-1)
else:
    print(result)
