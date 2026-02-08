def isOk(A: list[int], L: int)-> bool:
    if len(A) % 2 == 1:
         return False
    for i in range(len(A)):
        if A[i] + A[-i-1] != L:
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
# 全て折れている
L = A[0] + A[-1]
if isOk(A, L):
    result.add(L)
t = A[-1]
# 折れていないものが存在
memo = -1
for i in range(N):
    if t == A[i]:
        memo = i
        break
L = A[-1]
if memo > 0 and isOk(A[:memo], L):
        result.add(L)
result = sorted(list(result))
print(*result)
