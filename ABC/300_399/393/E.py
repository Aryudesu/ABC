N, K = map(int, input().split())
A = list(map(int, input().split()))

M = max(A)
s = [0] * (M + 1)
u = [0] * (M + 1)

for a in A:
    s[a] += 1

t = s[:]
for d in range(1, M + 1):
    for n in range(2 * d, M + 1, d):
        t[d] += s[n]

for d in range(1, M + 1):
    if t[d] < K:
        continue
    for n in range(d, M + 1, d):
        u[n] = max(u[n], d)

for a in A:
    print(u[a])
