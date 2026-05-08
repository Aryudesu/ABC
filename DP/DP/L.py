INF = 10 ** 18
N = int(input())
A = list(map(int, input().split()))
turn = N % 2 != 0
dp = dict()
for i in range(N):
    if turn:
        dp[(i, i)] = A[i]
    else:
        dp[(i, i)] = -A[i]
turn = not turn
for n in range(N-1):
    nextDP = dict()
    for key, value in dp.items():
        l, r = key
        if l - 1 >= 0:
            if turn:
                nextDP[(l - 1, r)] = max(nextDP.get((l - 1, r), -INF), value + A[l - 1])
            else:
                nextDP[(l - 1, r)] = min(nextDP.get((l - 1, r), INF), value - A[l - 1])
        if r + 1 < N:
            if turn:
                nextDP[(l, r + 1)] = max(nextDP.get((l, r + 1), -INF), value + A[r + 1])
            else:
                nextDP[(l, r + 1)] = min(nextDP.get((l, r + 1), INF), value - A[r + 1])
    turn = not turn
    dp = nextDP
print(dp[(0, N-1)])
