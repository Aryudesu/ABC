import heapq

N, K = [int(l) for l in input().split()]
data = []
a_data = []
b_data = []

heapq.heapify(data)
for i in range(N):
    a, b = [int(l) for l in input().split()]
    a_data.append(a)
    b_data.append(b)
    heapq.heappush(data, (-b, i))

result = 0
for _ in range(K):
    if not data:
        break
    num, idx = heapq.heappop(data)
    result += -num
    if idx is not None and idx >= 0:
        a = a_data[idx]
        b = b_data[idx]
        heapq.heappush(data, (-(a - b), -1))
print(result)
