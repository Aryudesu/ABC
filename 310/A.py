def calc(N, P, Q, D):
    if D[0] + Q < P:
        return D[0] + Q
    return P


N, P, Q = [int(l) for l in input().split()]
D = [int(l) for l in input().split()]
D.sort()
print(calc(N, P, Q, D))
