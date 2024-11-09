def calc(A):
    if A[0] == A[1]:
        if A[2] == A[3]:
            return 2
        return 1
    if A[1] == A[2]:
        return 1
    if A[2] == A[3]:
        return 1
    return 0

A = [int(l) for l in input().split()]
A.sort()
print(calc(A))
