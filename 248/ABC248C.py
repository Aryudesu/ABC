N, M, K = [int(l) for l in input().split()]
result = []
count = 1
result.append([1 for m in range(M + 1)])
result[0][0] = 0
for n in range(N - 1):
    tmp = [0 for m in range(M * (count + 1) + 1)]
    for m in range(M + 1):
        for l in range(M * (count) + 1):
            if not m or not l:
                continue
            tmp[m + l] += result[count - 1][l]
    result.append(tmp)
    count += 1

ans = 0
for k in range(K + 1):
    ans = (ans + result[N - 1][k]) % 998244353
print(ans)
