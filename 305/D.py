import bisect

N = int(input())
A = [int(l) for l in input().split()]
B = []
total = 0
for i in range(N):
    if i % 2 == 0:
        if i > 0:
            total += A[i] - A[i-1]
        B.append(total)
    else:
        B.append(total)
# print(A)
# print(B)
Q = int(input())
result = []
for _ in range(Q):
    l, r = [int(l) for l in input().split()]
    l_ = bisect.bisect_left(A, l)
    r_ = bisect.bisect_left(A, r)
    ls = 0
    if l_ == 0:
        ls = 0
    else:
        if l_ % 2 == 0:
            if A[l_] != l:
                ls = B[l_ - 1] + (l - A[l_ - 1])
            else:
                ls = B[l_]
        else:
            ls = B[l_ - 1]
    re = 0
    if r_ == N:
        re = B[-1]
    else:
        if r_ % 2 == 0:
            if A[r_] != r:
                re = B[r_] + (r - A[r_])
            else:
                re = B[r_]
        else:
            re = B[r_ - 1]
    # print(l_, r_, ls, re, re - ls)
    print(re - ls)
