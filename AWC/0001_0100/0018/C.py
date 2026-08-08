from collections import defaultdict

N, Q = map(int, input().split())
S = []
for n in range(N):
    S.append(input())

Sset = dict()
alp = "ABCDEFGHIJKLMNOPQRSTUVWXYZ".lower()
for a in alp:
    Sset[a] = set()
    Sset[a].add(a)

for _ in range(Q):
    a, b = input().split()
    aset: set = Sset[a]
    bset: set = Sset[b]
    if len(aset) > len(bset):
        aset.update(bset)
        bset = aset
    else:
        bset.update(aset)
    aset = set()
    Sset[a] = aset
    Sset[b] = bset
data = dict()
for key in Sset:
    chars = Sset[key]
    for c in chars:
        data[c] = key
result = []
for T in S:
    for t in T:
        print(data[t], end="")
    print()
