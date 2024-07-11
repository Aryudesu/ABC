import bisect

N, Q = [int(l) for l in input().split()]
TAB = []
User = dict()
res = []
for q in range(Q):
    T, A, B = [int(l) for l in input().split()]
    if T == 1:
        tmp = User.get(A)
        if tmp is None:
            tmp = dict()
        tmp[B] = True
        User[A] = tmp
    if T == 2:
        tmp = User.get(A)
        if tmp is None:
            tmp = dict()
        tmp[B] = False
        User[A] = tmp
    if T == 3:
        tmp = User.get(A)
        if tmp is None:
            res.append("No")
            continue
        tmp2 = tmp.get(B)
        if tmp2 is None:
            res.append("No")
            continue
        if tmp2:
            tmp3 = User.get(B)
            if tmp3 is None:
                res.append("No")
                continue
            tmp4 = tmp3.get(A)
            if tmp4 is None:
                res.append("No")
                continue
            if tmp4:
                res.append("Yes")
            else:
                res.append("No")
        else:
            res.append("No")
for r in res:
    print(r)
