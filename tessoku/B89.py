def calc(a: int, b: int, c: int) -> bool:
    if a == 1:
        return c > 1
    if c == 1:
        return False
    tmp = 1
    bTmp = 0
    while bTmp < b:
        if tmp > a:
            return True
        tmp *= c
        bTmp += 1
    return tmp > a

a, b, c = map(int, input().split())
print("Yes" if calc(a, b, c) else "No")
