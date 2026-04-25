def calc(A: list[int], N: int)->int:
    INF = 10**18
    dp = dict()
    turn = N % 2 != 0
    for n in range(N):
        if turn:
            dp[(n, n)] = A[n]
        else:
            dp[(n, n)] = -A[n]
    turn = not turn
    # print(dp)
    for n in range(N-1):
        nextDP = dict()
        for key in dp:
            l, r = key
            val = dp[key]
            if l - 1 >= 0:
                newL = l - 1
                if turn:
                    nextDP[(newL, r)] = max(nextDP.get((newL, r), -INF), val + A[newL])
                else:
                    nextDP[(newL, r)] = min(nextDP.get((newL, r), INF), val - A[newL])
            if r + 1 < N:
                newR = r + 1
                if turn:
                    nextDP[(l, newR)] = max(nextDP.get((l, newR), -INF), val + A[newR])
                else:
                    nextDP[(l, newR)] = min(nextDP.get((l, newR), INF), val - A[newR])
        dp = nextDP
        turn = not turn
        # print(dp)
    for key, val in dp.items():
        return val


INF = 10 ** 18
N = int(input())
A = list(map(int, input().split()))
S = sum(A)
res = calc(A, N)
# a + b = S, a - b = R  2a = S + R
taka = (S + res)//2
aoki = S - taka
print(taka, aoki)
