from collections import defaultdict

H, W, N = [int(l) for l in input().split()]
Xdata = defaultdict(set)
Ydata = defaultdict(set)
data = dict()
Xrmv_count = 0
Yrmv_count = 0
for n in range(N):
    X, Y = [int(l) for l in input().split()]
    Xdata[X].add(Y)
    Ydata[Y].add(X)
result = []
Q = int(input())
for _ in range(Q):
    n, x = [int(l) for l in input().split()]
    if n == 1:
        result.append(len(Xdata[x]))
        tmp = Xdata[x]
        for t in tmp:
            Ydata[t].discard(x)
        Xdata[x] = set()
    elif n == 2:
        result.append(len(Ydata[x]))
        tmp = Ydata[x]
        for t in tmp:
            Xdata[t].discard(x)
        Ydata[x] = set()
    else:
        raise Exception()
for r in result:
    print(r)
