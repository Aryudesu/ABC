from sortedcontainers import SortedList
from collections import defaultdict

N, K, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
hinshuCount = defaultdict(int)
hinshu = set()
height = SortedList()
result = 0
l = 0
for r in range(N):
    hinshuCount[A[r]] += 1
    hinshu.add(A[r])
    height.add(B[r])
    while len(hinshu) * (r - l + 1) > K or height[-1] - height[0] > M:
        height.discard(B[l])
        hinshuCount[A[l]] -= 1
        if hinshuCount[A[l]] == 0:
            hinshu.discard(A[l])
        l += 1
    result += r - l + 1
print(result)
