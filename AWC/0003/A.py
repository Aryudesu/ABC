N, K = map(int, input().split())
result = 0
for _ in range(N):
    a, b = map(int, input().split())
    if a * b >= K:
        result += 1

print(result)
