from collections import defaultdict

H, W = map(int, input().split())
G = []
Rdata = [defaultdict(int) for _ in range(H)]
Cdata = [defaultdict(int) for _ in range(W)]
for h in range(H):
    G.append(list(input()))
for h in range(H):
    for w in range(W):
        Rdata[h][G[h][w]] += 1
for w in range(W):
    for h in range(H):
        Cdata[w][G[h][w]] += 1
result = []
for h in range(H):
    for w in range(W):
        g = G[h][w]
        if Rdata[h][g] == 1 and Cdata[w][g] == 1:
            result.append(g)
print("".join(result))
