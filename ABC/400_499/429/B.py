N, M = [int(l) for l in input().split()]
A = [int(l) for l in input().split()]
S = sum(A)
if S - M in A:
    print("Yes")
else:
    print("No")
