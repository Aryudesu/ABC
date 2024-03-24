N, S = [l for l in input().split()]
N = int(N)
A, T, G, C = 0, 0, 0, 0
DA, DT, DG, DC = 0, 0, 0, 0
res = 0
for n in range(N):
    if S[n] == "A":
        A += 1
    if S[n] == "T":
        T += 1
    if S[n] == "G":
        G += 1
    if S[n] == "C":
        C += 1
    DA, DT, DG, DC = 0, 0, 0, 0
    for m in range(n):
        if m > 0:
            if S[m - 1] == "A":
                DA += 1
            if S[m - 1] == "T":
                DT += 1
            if S[m - 1] == "G":
                DG += 1
            if S[m - 1] == "C":
                DC += 1
        # print(A - DA, T - DT, G - DG, C - DC)
        if A - DA == T - DT and G - DG == C - DC:
            res += 1
print(res)
