def calc(X, Y, A):
    if X <= Y:
        for a in A:
            if a % (X + Y) >= X:
                return True
        return False
    else:
        for a in A:
            if a % (X + Y) >= Y:
                return False
        return True


N, X, Y = [int(l) for l in input().split()]
A = [int(l) for l in input().split()]
if calc(X, Y, A):
    print('First')
else:
    print('Second')
