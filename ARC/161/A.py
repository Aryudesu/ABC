def calc(N, A):
    DEBUG = False
    L = R = A[0]
    B = (N - 1)//2
    if DEBUG:
        print("B", B)
    for i in range(B):
        if i % 2:
            if DEBUG:
                print("Test", i, i + 1)
            if L > A[i] and R > A[i + 1]:
                L = A[i]
                R = A[i + 1]
            elif R > A[i] and L > A[i + 1]:
                R = A[i]
                L = A[i + 1]
            else:
                return False
        else:
            if DEBUG:
                print("Test", B + i + 1, B + i + 2)
            if B + i + 2 < N:
                if L < A[B + i + 1] and R < A[B + i + 2]:
                    L = A[B + i + 1]
                    R = A[B + i + 2]
                elif R < A[B + i + 2] and L < A[B + i + 1]:
                    R = A[B + i + 2]
                    L = A[B + i + 1]
                else:
                    return False
            else:
                if L < A[B + i + 1]:
                    L = A[B + i + 1]
                elif R < A[B + i + 1]:
                    R = A[B + i + 1]
                else:
                    return False
        if DEBUG:
            print(L, R)
    return True


N = int(input())
A = [int(l) for l in input().split()]
A.sort()
print("Yes" if calc(N, A) else "No")
