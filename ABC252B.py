N, K = [int(l) for l in input().split()]
A = [int(l) for l in input().split()]
B = [int(l) for l in input().split()]
AMax = 0
MaxIndex = []
res = False
for n in range(N):
    if AMax < A[n]:
        AMax = A[n]
        MaxIndex = []
    if AMax == A[n]:
        MaxIndex.append(n)
for k in range(K):
    if B[k] - 1 in MaxIndex:
        res = True
print("Yes" if res else "No")
