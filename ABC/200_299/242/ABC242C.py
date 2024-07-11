def countNum(N):
    res = [[1, 1, 1, 1, 1, 1, 1, 1, 1]]
    for num in range(1, N):
        tmp = []
        for k in range(9):
            if k == 0:
                tmp.append((res[num - 1][0] + res[num - 1][1]) % 998244353)
            elif k == 8:
                tmp.append((res[num - 1][8] + res[num - 1][7]) % 998244353)
            else:
                tmp.append(
                    (res[num - 1][k] + res[num - 1][k - 1] + res[num - 1][k + 1])
                    % 998244353
                )
        res.append(tmp)
    sum = 0
    for k in range(9):
        sum = (sum + res[N - 1][k]) % 998244353
    print(sum)


N = int(input())
countNum(N)
