H, W = map(int, input().split())
G = [list(map(int, input().split())) for _ in range(H)]
R = []
C = []
S = 0
for h in range(H):
    tmp = 0
    for w in range(W):
        tmp += G[h][w]
    R.append(tmp)
for w in range(W):
    tmp = 0
    for h in range(H):
        tmp += G[h][w]
    C.append(tmp)

result = -(10**18)
for h in range(H):
    for w in range(W):
        score = 0
        score += R[h]
        score += C[w]
        score -= G[h][w]
        result = max(result, score)
print(result)
