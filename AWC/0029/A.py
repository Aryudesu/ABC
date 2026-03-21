N, P, B, K = map(int, input().split())
C = list(map(int, input().split()))
result = 0
for c in C:
    result += c * P
    if c >= K:
        result += c * B
print(result)
