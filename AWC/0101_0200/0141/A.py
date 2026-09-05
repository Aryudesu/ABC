N, K, S, E = map(int, input().split())
result = 0
for n in range(N):
    t, h, b = map(int, input().split())
    if S <= t <= E and K <= h:
        result += b
print(result)
