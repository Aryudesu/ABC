def rev(S, N, L, R):
    res = ''
    for n in range(N):
        if n >= L and n <= R:
            tmp = S[R - (n - L)]
            res += 'p' if tmp == 'd' else 'd'
        else:
            res += S[n]
    return res


N = int(input())
S = input()
Fp = 0
FpF = True
pde = 0
Mp = set()
Pc = 0
MPc = 0
for i in range(N):
    if FpF:
        if S[i] == 'p':
            if not pde:
                Fp = i
                pde += 1
            else:
                pde += 1
        else:
            if Fp:
                FpF = False
    if S[- i - 1] == 'p':
        Pc += 1
    if Pc and S[- i - 1] == 'd':
        if MPc < Pc:
            MPc = Pc
            Mp = set()
        if MPc <= Pc:
            Mp.add(N - i + MPc - 1)
        Pc = 0
Mpc = Pc
Mp.add(Mpc - 1)
data = [S, rev(S, N, Fp, Fp + pde - 1)]
for mp in Mp:
    data.append(rev(S, N, Fp, mp))
data.sort()
print(data[0])
