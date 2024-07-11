H, W, N = [int(l) for l in input().split()]
Aset = set()
Bset = set()
Al = []
Bl = []
AB = dict()
for n in range(N):
    a, b = [int(l) for l in input().split()]
    if not a in Aset:
        Al.append(a)
        Aset.add(a)
    if not b in Bset:
        Bl.append(b)
        Bset.add(b)
    AB[n] = (a, b)
Al.sort()
Bl.sort()

Alen = len(Al)
Blen = len(Bl)
Ap = {Al[i]: i for i in range(Alen)}
Bp = {Bl[i]: i for i in range(Blen)}
for i in range(N):
    point = AB[i]
    print(Ap[point[0]] + 1, Bp[point[1]] + 1)
