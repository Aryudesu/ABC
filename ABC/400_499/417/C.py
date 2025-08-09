from collections import defaultdict

N = int(input())
A = [int(l) for l in input().split()]
result = 0
X = defaultdict(lambda: 0)
for i in range(N):
    tmp1 = A[i] - (i + 1)
    tmp2 = -(A[i] + (i + 1))
    # print(tmp2)
    X[tmp2] += 1
    result += X[tmp1]
# print(X)
print(result)
