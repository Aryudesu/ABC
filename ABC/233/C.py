N, X = [int(l) for l in input().split()]
A = []
for n in range(N):
    L, *a = [int(l) for l in input().split()]
    A.append(a)
dp = {1:1}
for n in range(N):
    new_dp = dict()
    for num in dp:
        for m in A[n]:
            tmp = m * num
            if X % tmp or X < tmp:
                continue
            new_dp[tmp] = dp.get(num, 0) + new_dp.get(tmp, 0)
    dp = new_dp
print(dp.get(X, 0))
