from atcoder.dsu import DSU
from collections import defaultdict

N = int(input())
A = list(map(int, input().split()))
dsu = DSU(N)
hights = sorted(set(A))
pos = defaultdict(list)

for idx in range(N):
    a = A[idx]
    pos[a].append(idx)

result = 0
leader = set()
prevh = None
while hights:
    h = hights.pop()
    if prevh is not None:
        result += len(leader) * (prevh - h)
    for idx in pos[h]:
        mergeF = False
        if idx - 1 >= 0 and A[idx - 1] >= h:
            l1 = dsu.leader(idx - 1)
            l2 = dsu.leader(idx)
            leader.discard(l1)
            leader.discard(l2)
            dsu.merge(idx - 1, idx)
            leader.add(dsu.leader(l1))
            mergeF = True
        if idx + 1 < N and A[idx + 1] >= h:
            l1 = dsu.leader(idx + 1)
            l2 = dsu.leader(idx)
            leader.discard(l1)
            leader.discard(l2)
            dsu.merge(idx + 1, idx)
            leader.add(dsu.leader(l1))
            mergeF = True
        if not mergeF:
            leader.add(idx)
    prevh = h
if prevh > 0:
    result += prevh
print(result)
