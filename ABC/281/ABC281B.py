def calc(S):
    S1 = S[0]
    S2 = S[1:-1]
    S3 = S[-1]
    if S1 not in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        return False
    try:
        if len(S2) != 6:
            return False
        n = int(S2)
        if n >= 100000 and n <= 999999:
            pass
        else:
            return False
    except:
        return False
    if S3 not in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        return False
    return True


print("Yes" if calc(input()) else "No")
