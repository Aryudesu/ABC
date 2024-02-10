from sortedcontainers import SortedList

N, K = [int(l) for l in input().split()]
P = [int(l) for l in input().split()]
data = SortedList()
result = []
for k in range(K-1):
    data.add(P[k])
for i in range(K, N + 1):
    data.add(P[i-1])
    result.append(data[-K])
for r in result:
    print(r)
