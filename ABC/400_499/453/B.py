T, X = map(int, input().split())
A = list(map(int, input().split()))
result = [(0, A[0])]
for t in range(1, T+1):
    if abs(result[-1][1] - A[t]) >= X:
        result.append((t, A[t]))
for res in result:
    print(*res)
