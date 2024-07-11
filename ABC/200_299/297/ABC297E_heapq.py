import heapq
N, K = [int(l) for l in input().split()]
A = [int(l) for l in input().split()]
data, d_set = [0], set()
heapq.heapify(data)
for i in range(K):
    m = heapq.heappop(data)
    for a in A:
        if not m + a in d_set:
            heapq.heappush(data, m + a), d_set.add(m + a)
print(heapq.heappop(data))
