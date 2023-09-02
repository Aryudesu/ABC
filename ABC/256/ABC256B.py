N = int(input())
A = [int(l) for l in input().split()]
B = 0
S = [0, 1, 1, 2, 1, 2, 2, 3, 1, 2, 2, 3, 2, 3, 3, 4]
P = 0
for a in A:
    tmpA = (B | 1) << a
    tmp = tmpA >> 4
    P += S[tmp]
    B = tmpA & 15
print(P)
