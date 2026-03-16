from collections import defaultdict
N, L, R = map(int, input().split())
S = input()
data = defaultdict(int)
for i in range(L, min(R + 1, N)):
    data[S[i]] += 1
result = 0
for i in range(N):
    result += data[S[i]]
    l = i + L
    r = i + R + 1
    if l < N:
        data[S[l]] -= 1
    if r < N:
        data[S[r]] += 1
print(result)
