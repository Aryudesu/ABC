INF = 10 ** 18
N = int(input())
A = list(map(int, input().split()))
takahashi = N % 2 == 0
dp = dict()
for n in range(N):
    dp[(n, n)] = A[n]
for _ in range(N-1):
    nextDP = dict()
    for key, value in dp.items():
        l, r = key
        if l - 1 >= 0:
            nextKey = (l-1, r)
            if takahashi:
                nextDP[nextKey] = max(nextDP.get(nextKey, -INF), value)
            else:
                nextDP[nextKey] = min(nextDP.get(nextKey, INF), value)
        if r + 1 < N:
            nextKey = (l, r+1)
            if takahashi:
                nextDP[nextKey] = max(nextDP.get(nextKey, -INF), value)
            else:
                nextDP[nextKey] = min(nextDP.get(nextKey, INF), value)
    takahashi = not takahashi
    dp = nextDP
print(dp[(0, N-1)])
