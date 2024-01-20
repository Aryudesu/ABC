def calc(S):
    l = 0
    r = len(S) - 1
    lc = 0
    rc = 0
    while True:
        if S[l] == "a":
            l += 1
            lc += 1
        if S[r] == "a":
            r -= 1
            rc += 1
        if l >= r:
            if lc > rc:
                return False
            return True
        if S[l] != "a" and S[r] != "a":
            break
    if lc > rc:
        return False
    while True:
        if S[l] == S[r]:
            l += 1
            r -= 1
        else:
            return False
        if l >= r:
            return S[l] == S[r]
    return True

S = input()
print("Yes" if calc(S) else "No")
