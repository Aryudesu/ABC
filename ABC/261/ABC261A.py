def calc(L1, R1, L2, R2):
    if L1 <= L2 and L2 <= R1 and R1 <= R2:
        return R1 - L2
    elif L2 <= L1 and R1 <= R2:
        return R1 - L1
    elif L2 <= L1 and L1 <= R2 and R2 <= R1:
        return R2 - L1
    elif L1 <= L2 and R2 <= R1:
        return R2 - L2
    return 0


L1, R1, L2, R2 = [int(l) for l in input().split()]
print(calc(L1, R1, L2, R2))
