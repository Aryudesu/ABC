def calc(S, T):
    if len(S) > len(T):
        S, T = T, S
    if len(S) == len(T):
        c = 0
        for i in range(len(S)):
            if S[i] != T[i]:
                c += 1
        return c <= 1
    elif len(S) + 1 == len(T):
        tidx = 0
        for sidx in range(len(S)):
            if S[sidx] != T[tidx]:
                if tidx >= sidx + 1:
                    return False
                else:
                    tidx += 1
                    if S[sidx] != T[tidx]:
                        return False
            tidx += 1
        return True
    else:
        return False


K = int(input())
S = input()
T = input()
print("Yes" if calc(S, T) else "No")
