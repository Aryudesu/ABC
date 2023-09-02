N = int(input())
S = list(input())
Q = int(input())
for q in range(Q):
    n, x, c = [l for l in input().split()]
    n = int(n)
    x = int(x)
    if n == 2:
        c = int(c)
    if n == 1:
        S[x-1] = c
