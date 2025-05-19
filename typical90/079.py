def calc(H, W, data):
    count = 0
    for h in range(H-1):
        for w in range(W-1):
            tmp = -data[h][w]
            data[h][w] += tmp
            data[h + 1][w] += tmp
            data[h][w + 1] += tmp
            data[h + 1][w + 1] += tmp
            count += abs(tmp)
    for h in range(H):
        for w in range(W):
            if data[h][w] != 0:
                return False, None
    return True, count

H, W = [int(l) for l in input().split()]
A = []
data = []
for h in range(H):
    A.append([int(l) for l in input().split()])
for h in range(H):
    tmp = [int(l) for l in input().split()]
    for w in range(W):
        tmp[w] = tmp[w] - A[h][w]
    data.append(tmp)
res, cnt = calc(H, W, data)
if res:
    print("Yes")
    print(cnt)
else:
    print("No")
