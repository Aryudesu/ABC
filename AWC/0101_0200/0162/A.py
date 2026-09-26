N, M = map(int, input().split())
S = list(map(int, input().split()))
data = [0] * N
for _ in range(M):
    t, p = map(int, input().split())
    if data[t-1] + p <= S[t-1]:
        data[t-1] += p
print(sum(d==s for d, s in zip(data, S)))
