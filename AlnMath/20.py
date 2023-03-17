N = input()
A = [int(l) for l in input().split()]
dp = [{} for _ in range(5)]
for a in A:
    new_dp = [{} for _ in range(5)]
    t_dp = new_dp[0]
    t_dp[a] = t_dp.get(a, 0) + 1
    for k in dp[0]:
        t_dp[k] = dp[0].get(k, 0) + t_dp.get(k, 0)
    for idx in range(1, 5):
        for n in dp[idx]:
            new_dp[idx][n] = dp[idx][n]
        prev = dp[idx - 1]
        for p_num in prev:
            tmp = a + p_num
            if tmp > 1000:
                continue
            num = new_dp[idx].get(tmp, 0) + new_dp[idx - 1].get(p_num, 0)
            new_dp[idx][tmp] = num
    dp = new_dp
    print(dp)
print(dp[4].get(1000, 0))
