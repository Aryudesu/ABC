N, K = map(int, input().split())
result = 0
now = int(input())
for n in range(N-1):
    t = int(input())
    if abs(now - t) >= K:
        result += 1
    now = t
print(result)
