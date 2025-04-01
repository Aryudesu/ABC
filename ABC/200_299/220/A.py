def calc(A, B, C):
    for i in range(1000):
        if A <= C * i <= B:
            return C * i
    return -1

A, B, C = [int(l) for l in input().split()]
print(calc(A, B, C))
