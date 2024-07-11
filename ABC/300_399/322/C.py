N, M = [int(l) for l in input().split()]
A = [int(l) for l in input().split()]
m = 0
for i in range(1, N + 1):
    a = A[m]
    print(a - i)
    if a == i:
        m += 1
