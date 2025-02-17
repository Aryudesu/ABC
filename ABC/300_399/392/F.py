from sortedcontainers import SortedSet

N = int(input())
P = [int(l) for l in input().split()]
P.reverse()
result = [None] * N
data = SortedSet(list(range(N)))
i = N
for p in P:
    idx = data[p - 1]
    data.discard(idx)
    result[idx] = i
    i -= 1
print(*result)
