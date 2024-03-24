def calc(N, Q, M):
    pass


N, Q = [int(l) for l in input().split()]
P = [int(l) for l in input().split()]
Tree = dict()
for i in range(N - 1):
    print(P[i])
    tmp = Tree.setdefault(P[i] - 1, [])
    tmp.append(i + 1)
    Tree[P[i] - 1] = tmp

M = []
res = []
for q in range(Q):
    tmp = [int(l) for l in input().split()]
    M = set(tmp[1:])
    print(M)
