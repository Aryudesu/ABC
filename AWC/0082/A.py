N, M, K = map(int, input().split())
A = list(map(int, input().split()))
result = 0
for m in range(M):
    s, p, d = map(int, input().split())
    kakaku = A[p-1]
    if s == 1:
        kakaku -= K
    result += max(kakaku, 0) * d
print(result)
