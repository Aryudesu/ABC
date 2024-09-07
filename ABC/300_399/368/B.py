N = int(input())
A = [int(l) for l in input().split()]
A.sort(reverse=True)
# print(A)
s = 0
for i in range(N):
    s += A[i]
if s - A[0] < A[0]:
    print(s - A[0])
else:
    print(s // 2)
