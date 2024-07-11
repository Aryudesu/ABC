import math
N = int(input())
A = [int(l) for l in input().split()]
g = math.gcd(A[0], A[1])
for n in range(2, N):
    g = math.gcd(g, A[n])
c = 0
for a in A:
    tmp = a
    while tmp != g:
        if tmp % 2 == 0 and (tmp//2) % g == 0:
            tmp //= 2
        elif tmp % 3 == 0 and (tmp//3) % g == 0:
            tmp //= 3
        else:
            print(-1)
            exit()
        c += 1
print(c)
