def calc2(v2, v3):
    result = []
    if v3 == 0:
        for a2 in range(8):
            for b2 in range(8):
                for c2 in range(8):
                    if abs(a2 * b2 * c2) == v2:
                        result.append((a2, b2, c2))
        if len(result) != 0:
            return True, result
        else:
            return False, None
    for a2 in range(8):
        for b2 in range(8):
            for c2 in range(8):
                if abs(a2 * b2 * c2) == v3:
                    result.append((a2, b2, c2))
    if len(result) != 0:
        return True, result
    else:
        return False, None

def calc3(v2, v3, a2, b2, c2):
    if v3 == 0:
        return 100, 100, 100
    for a3 in range(8 - a2):
        for b3 in range(8 - b2):
            for c3 in range(8 - c2):
                if abs((7 - a3) * (7 - b3) * (7 - c3)) + abs((7 - abs(a3 - a2)) * (b3 - b2) * (c3 - c2)) - v3 == v2:
                    return True, (a3, b3, c3)
    return False, None

def calc(v1, v2, v3):
    if v1 + v2 * 2 + v3 * 3 != 1029:
        return False, None
    a1, b1, c1 = 0, 0, 0
    res, data2 = calc2(v2, v3)
    if not res:
        return False, None
    for dat2 in data2:
        a2, b2, c2 = dat2
        res, data3 = calc3(v2, v3, a2, b2, c2)
        if res:
            a3, b3, c3 = data3
            return True, (a1, b1, c1, a2, b2, c2, a3, b3, c3)
    return False, None

V1, V2, V3 = [int(l) for l in input().split()]
res, data = calc(V1, V2, V3)
if res:
    print("Yes")
    print(*data)
else:
    print("No")
