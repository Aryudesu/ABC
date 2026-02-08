def isOk(A: list[int])-> bool:
    if len(A) % 2 == 1:
         return False
    tmp = A[0] + A[-1]
    for i in range(len(A)):
        if A[i] + A[-i-1] != tmp:
            return False
    return True

N = int(input())
A = list(map(int, input().split()))
A.sort()
result = set()
# 全部同じ値
tmp = set(A)
if len(tmp) == 1:
     result.add(A[0])
if isOk(A):
    result.add(A[0] + A[-1])
t = A[-1]
memo = -1
for i in range(N):
    if t == A[i]:
        memo = i
        break
if memo > 0 and isOk(A[:memo]):
        result.add(A[0] + A[memo-1])
result = sorted(list(result))
print(*result)
