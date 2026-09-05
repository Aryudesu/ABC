N, M, K, Q = map(int, input().split())
VC = []
for n in range(N):
    v, c = map(int, input().split())
    VC.append((v, c))
S = set(map(int, input().split()))
data = []
for v, c in VC:
    if c not in S:
        continue
    data.append(v)
data.sort(reverse=True)
print(sum(data[:K]))
