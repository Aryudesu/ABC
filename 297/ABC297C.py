H, W = [int(l) for l in input().split()]
S = []
for h in range(H):
    S.append(input())
result = []
for h in range(H):
    tmp = []
    th = False
    for w in range(W):
        if th:
            th = False
            continue
        if w < W - 1 and S[h][w] == "T" and S[h][w + 1] == "T":
            tmp.append("P")
            tmp.append("C")
            th = True
        else:
            tmp.append(S[h][w])
    result.append(tmp)
for r in result:
    print("".join(r))
