def calc(S):
    if S[0] == "R" and S[1] == "M":
        return True
    if S[0] == "R" and S[2] == "M":
        return True
    if S[1] == "R" and S[2] == "M":
        return True
    return False

S = input()
print("Yes" if calc(S) else "No")
