import fractions


def calc(r, N):
    r1, r2 = 10**10, 1
    for n in range(0, N):
        for m in range(n, N):
            if m == 0:
                break
            if abs(r - Decimal(r1)/Decimal(r2)) > abs(r - Decimal(n)/Decimal(m)):
                r1, r2 = n, m
            elif abs(r - Decimal(r1)/Decimal(r2)) == abs(r - Decimal(n)/Decimal(m)):
                if Decimal(r1)/Decimal(r2) > Decimal(n)/Decimal(m):
                    r1, r2 = n, m
    return r1, r2



r = Decimal(float(input()))
N = int(input())
r1, r2 = calc(r, N)
print(r1, r2)
