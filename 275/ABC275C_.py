def calc_dist2(a, b, c, d):
    return (a - c) ** 2 + (b - d) ** 2


def is_normal(a, b, c):
    if a * b * c == 0:
        return False
    return a + b - c == 0


def calc():
    s = [list(input()) for _ in range(9)]
    ans = 0
    for a in range(9):
        for b in range(9):
            for c in range(9):
                for d in range(9):
                    for e in range(9):
                        for f in range(9):
                            for g in range(9):
                                for h in range(9):
                                    if s[a][b] == '#' and s[c][d] == '#' and s[e][f] == '#' and s[g][h] == '#':
                                        abef = calc_dist2(a, b, e, f)
                                        abcd = calc_dist2(a, b, c, d)
                                        efgh = calc_dist2(e, f, g, h)
                                        cdgh = calc_dist2(c, d, g, h)
                                        efcd = calc_dist2(e, f, c, d)
                                        abgh = calc_dist2(a, b, g, h)
                                        # print(a, b, c, d, e, f, g, h)
                                        if abef == abcd and abcd == efgh and efgh == cdgh:
                                            if is_normal(abef, abcd, efcd) and is_normal(abef, efgh, abgh) and is_normal(cdgh, abcd, abgh) and is_normal(cdgh, efgh, efcd):
                                                ans += 1
    return ans


print(calc()//8)
