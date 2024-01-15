def makeMatrix(N, S):
    result = []
    lenN = len(N)
    for _ in range(lenN + 1):
        tmp1 = []
        for _ in range(S + 1):
            tmp2 = []
            for _ in range(S):
                tmp2.append([0, 0])
            tmp1.append(tmp2)
        result.append(tmp1)
    return result


def calc(N, S):
    dp = makeMatrix(N, S)
    dp[0][0][0][1] = 1
    lenN = len(N)
    # 1桁ずつループ
    for d in range(lenN):
        # 各桁についての走査
        for i in range(S + 1):
            # jで割った余りについての走査
            for j in range(S):
                # Nまで一致しているか
                for f in range(2):
                    # 0～9までに対しての走査
                    for t in range(10):
                        if i + t > s:
                            continue
                        if f and int(N[d]) < t:
                            continue
                        dp[d + 1][i + t][(j * 10 + t) % s][f and int(N[d]) == t] += dp[d][i][j][f]
    return dp[lenN][s][0][0] + dp[lenN][s][0][1]



N = input()
result = 0
for s in range(1, 9 * 14 + 1):
    result += calc(N, s)
print(result)
