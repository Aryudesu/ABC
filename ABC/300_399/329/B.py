N = int(input())
A = list({int(l) for l in input().split()})
A.sort(reverse=True)
print(A[1])
