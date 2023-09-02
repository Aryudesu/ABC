N = int(input())
d = dict()
res = []
for n in range(N):
    S = input()
    n = d.setdefault(S, 0)
    if n:
        res.append(f"{S}({n})")
    else:
        res.append(S)
    d[S] += 1
for r in res:
    print(r)
