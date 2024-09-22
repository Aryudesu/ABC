import heapq

N = int(input())
H = [int(l) for l in input().split()]
data = []
heapq.heapify(data)
H.reverse()
result = []
for h in H:
    result.append(len(data))
    while True:
        if len(data) == 0:
            heapq.heappush(data, h)
            break
        a = heapq.heappop(data)
        if h <= a:
            heapq.heappush(data, h)
            heapq.heappush(data, a)
            break

result.reverse()
print(*result)
