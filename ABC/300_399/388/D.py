N = int(input())
A = [int(l) for l in input().split()]
result = [0] * N
# i年には所持がゼロになる人のメモ
memo = dict()
# 渡せる人数
num = 0
for i in range(N):
    # A[i]の人が持っている石の個数
    n = A[i] + num
    result[i] = max([0, n - (N - i - 1)])
    if n > 0:
        num = num + 1 - memo.get(i, 0)
        memo[i + n] = memo.get(i + n, 0) + 1
    # print(n, num, memo)
print(*result)
