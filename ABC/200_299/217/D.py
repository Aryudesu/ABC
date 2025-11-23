from sortedcontainers import SortedSet
L, Q = map(int, input().split())
cutted = SortedSet()
cutted.add(0)
cutted.add(L)
result = []
for q in range(Q):
    c, x = map(int, input().split())
    if c == 1:
        cutted.add(x)
    elif c == 2:
        idx = cutted.bisect_left(x)
        result.append(cutted[idx] - cutted[idx-1])
    else:
        raise Exception()
for r in result:
    print(r)
