from atcoder.dsu import DSU
N = int(input())
T = [int(l) - 1 for l in input().split()]
dsu = DSU(N)
for n in range(N):
    dsu.merge(n, T[n])

result = 0
memo = set()
for n in range(N):
    l = dsu.leader(n)
    if l in memo:
        continue
    memo.add(l)
    result += dsu.size(n) - 1
print(result)
