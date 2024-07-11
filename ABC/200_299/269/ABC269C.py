N = int(input())
Nb = list(bin(N))[2:]
LNb = len(Nb)
Ones = []
Co1 = 0
for i in range(LNb):
    if Nb[i] == "1":
        Ones.append(i)
        Co1 += 1
res = []
for i in range(2 ** Co1):
    Ib = list(bin(i))[2:]
    LIb = len(Ib)
    Ib = ["0"] * (Co1 - LIb) + Ib
    for j in range(Co1):
        Nb[Ones[j]] = Ib[j]
    tmp = int('0b' + ''.join(Nb) , 2)
    res.append(tmp)
for r in res:
    print(r)
