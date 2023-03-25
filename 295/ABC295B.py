def is_bom(r, c, boms):
    for b in boms:
        if abs(r - b[0]) + abs(c - b[1]) <= b[2]:
            return True
    return False


def calc(R, C, B):
    boms = []
    nums = {"1", "2", "3", "4", "5", "6", "7", "8", "9"}
    for r in range(R):
        for c in range(C):
            if B[r][c] in nums:
                boms.append([r, c, int(B[r][c])])
    result = []
    for r in range(R):
        tmp = []
        for c in range(C):
            if is_bom(r, c, boms):
                tmp.append(".")
            else:
                tmp.append(B[r][c])
        result.append(tmp)
    return result


R, C = [int(l) for l in input().split()]
B = [input() for _ in range(R)]
result = calc(R, C, B)
for r in result:
    print("".join(r))
