from collections import defaultdict
N, K = map(int, input().split())
A = list(map(int, input().split()))
P = list(map(int, input().split()))
MOD = 10**9 + 7
if K == 1:
    print(A.count(P[0]) % MOD)
    exit(0)

chrIdx = defaultdict(list)
for idx in range(K-1, -1, -1):
    p = P[idx]
    chrIdx[p].append(idx)

# Pのうち何文字目となるのが何通り存在するか
data = [0] * K
for a in A:
    idxes = chrIdx[a]
    for idx in idxes:
        if idx == 0:
            data[idx] = (data[idx] + 1) % MOD
        else:
            data[idx] = (data[idx] + data[idx-1]) % MOD
print(data[-1])
