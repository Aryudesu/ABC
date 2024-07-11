N, M = [int(l) for l in input().split()]
S = []
res = 0
for n in range(N):
    tmp = input()
    S.append(tmp[3:])
# print(S)
T = set()
for m in range(M):
    tmp = input()
    T.add(tmp)
for s in S:
    if s in T:
        res += 1
print(res)
