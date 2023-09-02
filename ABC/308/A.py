def calc(S):
    bs = -1
    f = True
    for s in S:
        if bs > s:
            return False
        if s < 100:
            return False
        if s > 675:
            return False
        if s % 25:
            return False
        bs = s
    return True


S = [int(l) for l in input().split()]
print("Yes" if calc(S) else "No")
