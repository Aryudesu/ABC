from atcoder.dsu import DSU
from collections import defaultdict

MX = 200000 + 5
MOD = 998244353
frac = [1]
for n in range(1, MX + 1):
    frac.append((frac[-1] * n) % MOD)
N, M = map(int, input().split())
S = input()
dsu = DSU(N)
for m in range(M):
    a, b = map(int, input().split())
    a, b = a-1, b-1
    dsu.merge(a, b)
data = defaultdict(list)
for n in range(N):
    l = dsu.leader(n)
    data[l].append(S[n])

numer = 1
denom = 1
isDup = False
for l in data:
    dupMemo = dict()
    if len(data[l]) == 1:
        continue
    for s in data[l]:
        dupMemo[s] = dupMemo.get(s, 0) + 1

    numer = (numer * frac[len(data[l])]) % MOD
    for key, value in dupMemo.items():
        if value >= 2:
            denom = (denom * frac[value]) % MOD
            isDup = True

if isDup:
    print((numer * pow(denom, MOD-2, MOD)) % MOD)
else:
    print((numer * pow(2, MOD-2, MOD)) % MOD)
