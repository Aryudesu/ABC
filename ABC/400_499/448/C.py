from sortedcontainers import SortedList

N, Q = map(int, input().split())
A = list(map(int, input().split()))
balls = SortedList()
for idx in range(N):
    balls.add((A[idx], idx))
result = []
for _ in range(Q):
    K = int(input())
    B = list(map(int, input().split()))
    for b in B:
        balls.discard((A[b-1], b-1))
    result.append(balls[0][0])
    for b in B:
        balls.add((A[b-1], b-1))
for r in result:
    print(r)
