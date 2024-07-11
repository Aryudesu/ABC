N, M = [int(l) for l in input().split()]
S = input()
C = [int(l) for l in input().split()]
data = dict()
for n in range(N):
    c = C[n]
    tmp = data.get(c, [])
    tmp.append(S[n])
    data[c] = tmp
idx = [-1] * (M + 1)
result = []
for c in C:
    tmp = data.get(c, [])
    result.append(tmp[idx[c]])
    idx[c] = (idx[c] + 1) % len(tmp)
print("".join(result))
