def calc(N: int, V: list[int]):
    INF = 10 ** 18
    dp = dict()
    # 2の倍数なら後手が最後
    turn = N % 2 != 0
    for n in range(N):
        if turn:
            dp[(n, n)] = V[n]
        else:
            dp[(n, n)] = -V[n]
    turn = not turn
    for n in range(N-1):
        nextDP = dict()
        for key, value in dp.items():
            l, r = key
            if l - 1 >= 0:
                newL = l - 1
                newKey = (newL, r)
                if turn:
                    nextDP[newKey] = max(nextDP.get(newKey, -INF), value + V[newL])
                else:
                    nextDP[newKey] = min(nextDP.get(newKey, INF), value - V[newL])
            if r + 1 < N:
                newR = r + 1
                newKey = (l, newR)
                if turn:
                    nextDP[newKey] = max(nextDP.get(newKey, -INF), value + V[newR])
                else:
                    nextDP[newKey] = min(nextDP.get(newKey, INF), value - V[newR])
        turn = not turn
        dp = nextDP
    return sum(dp.values())

N = int(input())
V = list(map(int, input().split()))
print(calc(N, V))
