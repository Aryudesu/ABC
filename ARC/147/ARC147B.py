def calcB(N, P):
    res = []
    sortnum = 0
    for _ in range(N):
        for j in range(N):
            if j + 2 >= N:
                continue
            if P[j] > P[j + 2]:
                P[j], P[j + 2] = P[j + 2], P[j]
                sortnum += 1
                res.append(f'B {j + 1}')
    return sortnum, res


def calcA(P, M20, M21):
    idx = 0
    sortnum = 0
    res = []
    while len(M20) > idx:
        # 2つを隣同士の関係にしたい
        M0 = M20[idx] - 1
        M1 = M21[idx] - 1
        c = 1
        if M0 > M1:
            if abs(M0 - M20[idx]) > abs(M1 - M21[idx]) or M1 < N - 2:
                while M0 - M1 != 1:
                    res.append(f'B {M0 + 1 - 2}')
                    P[M0], P[M0 - 2] = P[M0 - 2], P[M0]
                    sortnum += 1
                    M0 -= 2
                    c += 1
            else:
                while M0 - M1 != 1:
                    res.append(f'B {M1 + 1}')
                    P[M1], P[M1 + 2] = P[M1 + 2], P[M1]
                    sortnum += 1
                    M1 += 2
                    c += 1
        elif M0 < M1:
            if abs(M0 - M20[idx]) < abs(M1 - M21[idx]) or M0 < N - 2:
                while M1 - M0 != 1:
                    res.append(f'B {M1 + 1 - 2}')
                    P[M1 - 2], P[M1] = P[M1], P[M1 - 2]
                    sortnum += 1
                    M1 -= 2
                    c += 1
            else:
                while M1 - M0 != 1:
                    res.append(f'B {M0 + 1}')
                    P[M0 + 2], P[M0] = P[M0], P[M0 + 2]
                    sortnum += 1
                    M0 += 2
                    c += 1
        if M0 > M1:
            M0, M1 = M1, M0
        res.append(f'A {M0 + 1}')
        P[M1], P[M0] = P[M0], P[M1]
        sortnum += 1
        idx += 1
    return sortnum, res



N = int(input())
P = [int(l) for l in input().split()]
IdxMOD20 = []
IdxMOD21 = []
for n in range(N):
    if P[n] % 2 != (n + 1) % 2:
        if (n + 1) % 2 == 1:
            IdxMOD21.append(n + 1)
        else:
            IdxMOD20.append(n + 1)
res_num = 0
res_num1, res1 = calcA(P, IdxMOD20, IdxMOD21)
res_num2, res2 = calcB(N, P)
print(res_num1 + res_num2)
if res1:
    for res in res1:
        print(res)
if res2:
    for res in res2:
        print(res)
