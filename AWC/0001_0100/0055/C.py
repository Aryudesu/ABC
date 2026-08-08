from heapq import heappop, heappush, heapify

N = int(input())
W = [-int(l) for l in input().split()]
C = list(map(int, input().split()))
C.sort(reverse=True)
heapify(W)
result = 0
for c in C:
    while W:
        w = -heappop(W)
        if c >= w:
            result += 1
            break
print(result)
