from collections import defaultdict

N, K = map(int, input().split())
A = list(map(int, input().split()))
S = sum(A)
Adata = defaultdict(int)
for a in A:
    Adata[a] += a
data = []
for k, n in Adata.items():
    data.append(n)
data.sort(reverse=True)
print(S - sum(data[:K]))
