from heapq import heappush, heappop

N = int(input())
A = list(map(int, input().split()))
data = []
for a in A:
    heappush(data, -a)
result = 0
turn = 1
while data:
    n = -heappop(data)
    result += n * turn
    turn = -turn
print(result)
