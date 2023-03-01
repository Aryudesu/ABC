N = input()
A = [int(l) for l in input().split()]
dp = [{0: 0}, {}, {}, {}, {}]
for a in A:
    new_dp = [{0: 0}, {}, {}, {}, {}]
    for i in range(4):
        data1 = dp[i]
        ndata1 = new_dp[i]
        ndata2 = new_dp[i + 1]
        for dat in data1:
            pass
