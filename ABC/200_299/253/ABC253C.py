import bisect

Q = int(input())
d = dict()
res = []
keys = []
for idx in range(Q):
    q = [int(l) for l in input().split()]
    if q[0] == 1:
        x = str(q[1])
        n = d.setdefault(x, 0)
        if not n:
            bisect.insort(keys, q[1])
        d[x] = n + 1
    elif q[0] == 2:
        x = str(q[1])
        c = q[2]
        n = d.get(x, 0)
        if c < n:
            d[x] = n - c
        else:
            d[x] = 0
            i = bisect.bisect_left(keys, q[1])
            if len(keys) <= i:
                continue
            if keys[i] == q[1]:
                del keys[i]
    elif q[0] == 3:
        print(keys[-1] - keys[0])
