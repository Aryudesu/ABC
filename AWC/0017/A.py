N, K = map(int, input().split())
result = 0
for n in range(N):
    c, d = map(int, input().split())
    if c > K:
        continue
    result += d
print(result)
