def calc(N, M, X, T, D):
    res = 0
    if M >= X:
        return T
    else:
        return T - D * (X - M)


N, M, X, T, D = [int(l) for l in input().split()]
print(calc(N, M, X, T, D))
