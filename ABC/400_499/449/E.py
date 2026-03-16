from heapq import heappop, heappush
from collections import defaultdict

N, M = map(int, input().split())
A = list(map(int, input().split()))
Q = int(input())
data = defaultdict(int)
for a in A:
    data[a] += 1
print(data)
for _ in range(Q):
    X = int(input())
