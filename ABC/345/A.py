def calc(S):
    SN = len(S)
    for idx in range(1, SN - 1):
        if S[idx] != "=":
            return False
    return S[0] == "<" and S[-1] == ">"

print("Yes" if calc(input()) else "No")

