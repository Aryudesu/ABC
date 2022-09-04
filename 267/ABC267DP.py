N, M = [int(l) for l in input().split()]
A = [int(l) for l in input().split()]

prev_dp = [A[m] for m in range(N - M + 1)]
# M個選ぶ
for m in range(1, M):
    next_dp = []
    idxmax = 0
    # 今回までの結果
    for idx1 in range(m - 1, N - M + m):
        # 次に選ぶもの
        for idx2 in range(idx1 + 1, N - M + m + 1):
            previdx = idx1 - m + 1
            nextidx = idx2 - m
            tmp = prev_dp[previdx] + (m + 1) * A[idx2]
            if idxmax <= nextidx:
                next_dp.append(tmp)
                idxmax += 1
            elif tmp > next_dp[nextidx]:
                next_dp[nextidx] = tmp
    prev_dp = next_dp
print(max(prev_dp))
