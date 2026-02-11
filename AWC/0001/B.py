N, L, R = map(int, input().split())
P = list(map(int, input().split()))
m = -1
result = -1
for idx in range(N):
    p = P[idx]
    if L <= p <= R and m < p:
        m = p
        result = idx + 1
print(result)
