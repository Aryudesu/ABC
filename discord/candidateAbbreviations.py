from itertools import product

N, M = map(int, input().split())
S = input()
result = set()
for dat in product([0, 1], repeat = N):
    c = 0
    tmp = []
    for i in range(N):
        if dat[i] == 0:
            continue
        c += 1
        tmp.append(S[i])
    if 1 <= c <= M:
        result.add("".join(tmp))
print(len(result))
print(sorted(result))
