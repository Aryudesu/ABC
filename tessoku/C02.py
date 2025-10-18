N = int(input())
A = [int(l) for l in input().split()]
A.sort()
print(A[-1] + A[-2])
