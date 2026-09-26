H, W = map(int, input().split())
R, C = map(int, input().split())
data = dict()
for h in range(H):
    G = input()
    for w in range(W):
        g = G[w]
        tmp = data.get(g, [])
        tmp.append((h, w))
        data[g] = tmp
N = int(input())
S = input()

INF = 10 ** 18
dp = [INF] * (H * W)
dp[(R-1)*W + (C-1)] = 0
for idx in range(N):
    nextDP = [INF] * (H * W)
    s = S[idx]
    if s not in data:
        print(-1)
        exit(0)
    for idx2 in range(H*W):
        ph, pw = idx2 // W, idx2 % W
        value = dp[idx2]
        for h, w in data[s]:
            nextValue = value + abs(h - ph) + abs(w - pw) + 1
            nextDP[h*W + w] = min(nextDP[h*W + w], nextValue)
    dp = nextDP
print(min(dp))
