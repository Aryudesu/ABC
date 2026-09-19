N, M, S, T = map(int, input().split())
result = 0
for _ in range(M):
    p, v = map(int, input().split())
    if S <= p <= T or T <= p <= S:
        result += v
print(result)
