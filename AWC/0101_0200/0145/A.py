N, M, P = map(int, input().split())
result = 0
for n in range(N):
    d, v = map(int, input().split())
    if d <= M:
        result += v
print(result * (100 - P) // 100)
