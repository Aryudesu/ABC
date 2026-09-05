N, K, Q = map(int, input().split())
S = [list(input()) for _ in range(N)]
memoData = [["0"] * K for _ in range(K)]

for _ in range(Q):
    r, c = map(int, input().split())
    r, c = r - 1, c - 1
    for h in range(K):
        for w in range(K):
            memoData[h][w] = S[r + K - w - 1][c + h]
    for h in range(K):
        for w in range(K):
            S[r + h][c + w] = memoData[h][w]
for s in S:
    print("".join(s))
