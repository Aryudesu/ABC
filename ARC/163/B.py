N, M = [int(l) for l in input().split()]
A = [int(l) for l in input().split()]
B = []
ma = 0
for i in range(2, N):
    if ma < A[i]:
        ma = A[i]
    B.append(A[i])
B.sort()
result = ma * N
# print(B)
for i in range(N - 2 - M + 1):
    l = B[i]
    r = B[i + M - 1]
    # print(l, r)
    tmp = 0
    if l < A[0]:
        tmp += abs(l - A[0])
    if r > A[1]:
        tmp += abs(r - A[1])
    if result > tmp:
        result = tmp
print(result)
