from heapq import heappush, heappop

Q = int(input())
data = []
result = []
minus = 0
for _ in range(Q):
    n, h = map(int, input().split())
    if n == 1:
        heappush(data, h)
    elif n == 2:
        while data:
            t = heappop(data)
            if t > h:
                heappush(data, t)
                break
    else:
        raise ValueError()
    result.append(len(data))
for r in result:
    print(r)
