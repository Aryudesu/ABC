import heapq

N, K = [int(l) for l in input().split()]
data = []
a_data = []
b_data = []
for i in range(N):
    a, b = [int(l) for l in input().split()]
    a_data.append(a)
    b_data.append(b)
    data.append((-b, i))
heapq.heapify(data)

result = 0
for _ in range(K):
    num, idx = heapq.heappop(data)
    result += -num
    if not idx is None:
        heapq.heappush(data, (-(a_data[idx]-b_data[idx]), None))
print(result)
