def calc(S):
    idx = S.find("o")
    if idx == -1 and len(S) >= 3:
        return False
    for i in range(len(S)):
        if idx == i:
            if S[i] != "o":
                return False
            idx += 3
        else:
            if S[i] != "x":
                return False
    return True


S = input()
print("Yes" if calc(S) else "No")
