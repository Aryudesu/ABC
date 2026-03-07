N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
dir = [-1, 0, 1]
for b in B:
    for d in dir:
        if not (0 <= b - 1 + d < N):
            continue
        A[b - 1 + d] += 1
print(*A)
