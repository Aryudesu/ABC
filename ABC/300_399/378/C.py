N = int(input())
A = [int(l) for l in input().split()]
B = []
memo = dict()
for n in range(N):
    tmp = memo.get(A[n], -1)
    B.append(tmp)
    memo[A[n]] = n + 1
print(*B)
