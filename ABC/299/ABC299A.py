def calc(S):
    f = False
    for s in S:
        if s == "|":
            f = not f
        if f and s == "*":
            return True
    return False


N = int(input())
S = input()
print("in" if calc(S) else "out")
