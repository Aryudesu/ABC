from collections import defaultdict

N = int(input())
A = [int(l) for l in input().split()]
lSet = set()
rSet = set()
rCount = defaultdict(lambda: 0)
lSet.add(A[0])
for i in range(1, N):
    rCount[A[i]] += 1
    rSet.add(A[i])
result = len(lSet) + len(rSet)
for i in range(1, N):
    a = A[i]
    rCount[a] -= 1
    lSet.add(a)
    if rCount[a] == 0:
        rSet.discard(a)
    result = max(result, len(lSet) + len(rSet))
print(result)
