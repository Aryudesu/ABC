def calc(S):
    data = [""] * len(S)
    idx = -1
    for s in S:
        if idx < 0:
            data[0] = s
            idx = 0
        else:
            if s == ")":
                if data[idx] == "(":
                    idx -= 1
                else:
                    return False
            elif s == "(":
                data[idx + 1] = s
                idx += 1
            if s == "]":
                if data[idx] == "[":
                    idx -= 1
                else:
                    return False
            elif s == "[":
                data[idx + 1] = s
                idx += 1
            if s == ">":
                if data[idx] == "<":
                    idx -= 1
                else:
                    return False
            elif s == "<":
                data[idx + 1] = s
                idx += 1
    return idx == -1



print("Yes" if calc(input()) else "No")
