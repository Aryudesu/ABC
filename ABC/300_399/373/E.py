N, M, K = [int(l) for l in input().split()]
A = [int(l) for l in input().split()]
nowNum = sum(A)
data = [(A[i], i)for i in range(N)]
data.sort(reverse=True)
print(data, nowNum)
