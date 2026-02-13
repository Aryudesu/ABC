from sortedcontainers import SortedSet
from collections import defaultdict

N, K = map(int, input().split())
A = list(map(int, input().split()))
counter = defaultdict(int)
data1 = SortedSet()
for a in A:
    data1.add(a)
    counter[a] += 1
data2 = defaultdict(set)
for i in range(N):
    a = A[i]
    data2[a].add(i)
result = 0
while data1:
    d = data1.pop(-1)
    idxes = data2[d]
    for idx in idxes:
        if idx - 1 >= 0:
            l = A[idx - 1]
            if l < d - K:
                counter[l] -= 1
                if counter[l] == 0:
                    data1.discard(l)
                data2[l].discard(idx - 1)
                result += d - K - l
                l = d - K
                data1.add(l)
                data2[l].add(idx - 1)
                A[idx - 1] = l
        if idx + 1 < N:
            r = A[idx + 1]
            if r < d - K:
                counter[r] -= 1
                if counter[r] == 0:
                    data1.discard(r)
                data2[r].discard(idx + 1)
                result += d - K - r
                r = d - K
                data1.add(r)
                data2[r].add(idx + 1)
                A[idx + 1] = r
print(result)
