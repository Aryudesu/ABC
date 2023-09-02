R, C = [int(l) for l in input().split()]
A = []
for i in range(2):
    A.append([int(l) for l in input().split()])
print(A[R-1][C-1])
