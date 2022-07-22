import math
 
X, A, D, N =  [int(l) for l in input().split()]
tmp = A + D * (N - 1)
tmp2 = A
if tmp > tmp2:
    max = tmp
    min = tmp2
else:
    max = tmp2
    min = tmp
if X >= min and X <= max:
    if D != 0:
        n1 = (X-A)//D
        n2 = n1 + 1
        if n1 < N and n1 >= 0:
            an1 = A + D * n1
        elif n1 >= N:
            an1 = A + D * (N - 1)
        else:
            an1 = A
        if n2 < N and n2 >= 0:
            an2 = A + D * n2
        elif n2 >= N:
            an2 = A + D * (N - 1)
        else:
            an2 = A
    else:
        an1 = A
        an2 = A
    if abs(X - an1) < abs(an2 - X):
        print(abs(X - an1))
    else:
        print(abs(an2 - X))
elif X < min:
    print(abs(min - X))
elif X > max:
    print(abs(X - max))
