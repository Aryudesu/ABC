T = int(input())
dst = [(1, 1), (1, 0), (0, 1), (0, 0)]
result = []
for t in range(T):
    H, W = [int(l) for l in input().split()]
    S = []
    count = 0
    for h in range(H):
        S.append(list(input()))
    data = [[0] * W for h in range(H)]
    for h in range(H - 1):
        for w in range(W - 1):
            f = True
            for dh, dw in dst:
                if S[h + dh][w + dw] == ".":
                    f = False
                    break
            if f:
                for dh, dw in dst:
                    if S[h + dh][w + dw] == "#":
                        data[h + dh][w + dw] += 1
    for h in range(H - 1):
        for w in range(W - 1):
            f = True
            for dh, dw in dst:
                if S[h + dh][w + dw] == ".":
                    f = False
                    break
            g = False
            if f:
                for dh, dw in dst:
                    if data[h + dh][w + dw] > 1:
                        S[h + dh][w + dw] = "."
                        data[h + dh][w + dw] = 0
                        g = True
                        count += 1
                        break
            if f and not g:
                S[h + 1][w + 1] = "."
                data[h + 1][w + 1] = 0
                count += 1
    result.append(count)
for r in result:
    print(r)
