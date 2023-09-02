import itertools

N, M = [int(l) for l in input().split()]
S = []
T = dict()


def saiki(S, num):
    pass


for n in range(N):
    S.append(input())

for m in range(M):
    Ti = input()
    if Ti[0] == '_':
        continue
    c = 0
    for t in Ti:
        if t == '_':
            c += 1
    tmp3 = Ti.replace('_', '')
    tmp = T.setdefault(tmp3, dict())
    tmp2 = tmp.setdefault(c, 0)
    tmp[c] = tmp2 + 1

for pn in itertools.permutations(S):
    tmp = ''.join(pn)
    L = 16 - len(tmp)
    for l in range(1, L + 1):
        pass
