def calcProb(A, B, C, X):
    if X <= A:
        return 1
    if X > A and X <= B:
        return C / (B - A)
    return 0


A, B, C, X = [int(l) for l in input().split()]
print(calcProb(A, B, C, X))
