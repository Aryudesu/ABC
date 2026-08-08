N, M = map(int, input().split())
A = list(map(int ,input().split()))
result = 0
for a in A:
    if 0 <= a <= M:
        continue
    result += min(abs(0-a), abs(M-a))
print(result)
