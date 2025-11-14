from sortedcontainers import SortedSet
from collections import defaultdict

N = int(input())
data = defaultdict(SortedSet)
A = list(map(int, input().split()))
for idx in range(N):
    data[A[idx]].add(idx + 1)
result = []
D = int(input())
for d in range(D):
    l, r = map(int, input().split())
    for num in range(100, -1, -1):
        if len(data[num]) > 0:
            m, M = data[num][0], data[num][-1]
            if not (l <= m <= M <= r):
                result.append(num)
                break
for r in result:
    print(r)
