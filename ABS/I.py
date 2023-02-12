def is_st_str(S, sl, idx, st):
    lst = len(st)
    if idx + lst > sl:
        return False
    for i in range(lst):
        if S[idx + i] != st[i]:
            return False
    return True


def calc(S):
    SL = len(S)
    idx = 0
    dream = "dream"
    erase = "erase"
    while idx < SL:
        if is_st_str(S, SL, idx, dream):
            idx += 5
            if idx + 2 <= SL:
                if S[idx] == "e" and S[idx + 1] == "r":
                    if idx + 3 <= SL:
                        if (S[idx + 2] == "e" or S[idx + 2] == "d"):
                            idx += 2
                    else:
                        idx += 2
        elif is_st_str(S, SL, idx, erase):
            idx += 5
            if idx + 1 <= SL:
                if S[idx] == "r":
                    idx += 1
        else:
            return "NO"
    return "YES"


S = input()
print(calc(S))
