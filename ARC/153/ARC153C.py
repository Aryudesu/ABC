def calc():
    N = int(input())
    A = [int(l) for l in input().split()]
    SA = sum(A)
    B = [SA]
    for i in range(1, N):
        B.append(B[i-1] - A[i - 1])
    print(B)


calc()
