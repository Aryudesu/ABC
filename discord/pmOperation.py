from collections import defaultdict

def calc(N: int, K: int, A: list[int])->int:
    INF = 10 ** 18
    S = sum(A)
    if (S - K) % 2 == 1:
        return -1
    if S < K:
        return -1
    M = (S - K) // 2
    dp = defaultdict(lambda: INF)
    dp[0] = 0
    for a in A:
        newDP = dp.copy()
        for num in dp:
            nextNum = num + a
            if nextNum > M:
                continue
            count = dp[num]
            if newDP[nextNum] <= count + 1:
                continue
            newDP[nextNum] = count + 1
        dp = newDP
    if M not in dp:
        return -1
    return dp[M]

N, K = map(int, input().split())
A = list(map(int, input().split()))
print(calc(N, K, A))
