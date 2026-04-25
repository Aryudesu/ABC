N, M = map(int, input().split())
data = [0] * (N + 1)
S = list(map(int, input().split()))
for m in range(M):
    l, r, w = map(int, input().split())
    data[l-1] += w
    data[r] -= w
result = 0
s = 0
for i in range(N):
    s += data[i]
    if S[i] < s:
        result += 1
print(result)
