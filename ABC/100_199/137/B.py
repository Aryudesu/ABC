from sortedcontainers import SortedSet

K, X = [int(l) for l in input().split()]
memo = SortedSet()
for i in range(K):
    memo.add(X + i)
    memo.add(X - i)
print(*memo)
