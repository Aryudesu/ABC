def calc(S, T):
    lS = len(S)
    lT = len(T)
    ml = min([lS, lT])
    for i in range(ml):
        if S[i] != T[i]:
            return i + 1
    if lS == lT:
        return 0
    return ml + 1

S = input()
T = input()
print(calc(S, T))
