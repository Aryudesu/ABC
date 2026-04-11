N, M, S = map(int, input().split())
P = list(map(int, input().split()))
result = S
for m in range(M):
    t, q = map(int, input().split())
    X = P[t-1] * q
    result += X - X//2
print(result)
