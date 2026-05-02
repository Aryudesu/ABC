def calc(S: str, T: str)->bool:
    f = False
    i = 0
    while i < len(S):
        if i + 1 < len(S) and S[i] != T[i]:
            if S[i + 1] == T[i] and S[i] == T[i + 1] and not f:
                f = True
                i += 1
            else:
                return False
        i += 1
    return True

S = input()
T = input()
print("Yes" if calc(S, T) else "No")
