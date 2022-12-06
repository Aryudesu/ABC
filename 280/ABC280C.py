def calc(S, T):
    slen = len(S)
    for idx in range(slen):
        if S[idx] != T[idx]:
            return idx + 1
    return slen + 1


S = input()
T = input()
print(calc(S, T))
