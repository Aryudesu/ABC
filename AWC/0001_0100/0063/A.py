H, W = map(int, input().split())
S = [input() for _ in range(H)]
result = []
for h in range(H):
    for w in range(W):
        if S[h][w] == "T":
            result.append((h + 1, w + 1))

print(len(result))
for h, w in result:
    print(h, w)
