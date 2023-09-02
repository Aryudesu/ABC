def calc(A, B, C, T):
    ABAT = (B[0] - A[0]) * (T[1] - A[1]) - (B[1] - A[1]) * (T[0] - A[0])
    BCBT = (C[0] - B[0]) * (T[1] - B[1]) - (C[1] - B[1]) * (T[0] - B[0])
    CACT = (A[0] - C[0]) * (T[1] - C[1]) - (A[1] - C[1]) * (T[0] - C[0])
    if ((ABAT > 0 and BCBT > 0 and CACT > 0) or (ABAT < 0 and BCBT < 0 and CACT < 0)):
        return False
    return True


A = [int(l) for l in input().split()]
B = [int(l) for l in input().split()]
C = [int(l) for l in input().split()]
D = [int(l) for l in input().split()]

if (calc(A, B, C, D) and calc(B, C, D, A) and calc(C, D, A, B) and calc(D, A, B, C)):
    print('Yes')
else:
    print('No')
