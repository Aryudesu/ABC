import bisect

N, M = [int(l) for l in input().split()]
A = [int(l) for l in input().split()]
A.sort()
# print(A)
result = 0
for n in range(N):
    a = A[n]
    tmp = bisect.bisect_right(A, a + M - 1)
    if tmp - n > result:
        result = tmp - n
    # print(tmp - n)
print(result)
