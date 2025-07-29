def calc(S):
    result = ""
    putF = False
    for s in S:
        if s == "#":
            putF = False
            result += "#"
        elif s == ".":
            if not putF:
                result += "o"
                putF = True
            else:
                result += "."
    return result

S = input()
print(calc(S))
