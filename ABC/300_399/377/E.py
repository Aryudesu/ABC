N, K = [int(l) for l in input().split()]
P = [int(l) - 1 for l in input().split()]
data = set()
while True:
    P = [P[P[k]] for k in range(N)]
    tp = tuple(P)
    if tp in data:
        break
    data.add(tp)
