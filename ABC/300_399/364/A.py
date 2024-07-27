def calc(N, IPT):
    f = False
    GO = False
    for ipt in IPT:
        if GO:
            return False
        S = ipt
        if S[-1] == "t":
            if f:
                GO = True
            f = True
        else:
            f = False
    return True


N = int(input())
IPT = []
for n in range(N):
    IPT.append(input())
print("Yes" if calc(N, IPT) else "No")
