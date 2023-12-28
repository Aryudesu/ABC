def calc(A, M, L, R):
    D1 = abs(L - A) // M
    D2 = abs(R - A) // M
    if L <= A and A <= R:
        print(D1 + D2 + 1)
    elif A <= L and A <= R:
        if (L - A) % M == 0:
            print(D2 - D1 + 1)
        else:
            print(D2 - D1)
    elif L < A and R < A:
        if (A - R) % M == 0:
            print(D1 - D2 + 1)
        else:
            print(D1 - D2)
    else:
        print(0)


A, M , L, R = [int(l) for l in input().split()]
calc(A, M, L, R)
