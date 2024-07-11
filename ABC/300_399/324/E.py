N, T = [l for l in input().split()]
N = int(N)
Dat1 = [0] * (len(T) + 2)
Dat2 = [0] * (len(T) + 2)
for n in range(N):
    ipt = input()
    idx1 = 0
    idx2 = 0
    dat1 = []
    dat2 = []
    for i in range(len(ipt)):
        if idx1 < len(T):
            if T[idx1] == ipt[i]:
                dat1.append(idx1)
                idx1 += 1
        if idx2 < N:
            if -i - 1 >= -len(ipt) and idx2 < len(T):
                if T[-idx2-1] == ipt[-i - 1]:
                    dat2.append(len(T) - idx2 - 1)
                    idx2 += 1
    if dat1:
        Dat1[dat1[-1] + 1] += 1
    else:
        Dat1[0] += 1
    if dat2:
        Dat2[dat2[-1] + 1] += 1
    else:
        Dat2[-1] += 1
d1 = 0
d2 = sum(Dat2)
result = 0
for i in range(len(T)):
    d1 += Dat1[i]
    result += d1 * d2
    d2 -= Dat2[i + 2]
print(Dat1)
print(Dat2)
print(N**2 - result)
