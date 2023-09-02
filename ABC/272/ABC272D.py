import math

N, M = [int(l) for l in input().split()]
XY = []
for x in range(M + 1):
    if M >= x**2:
        # yy = math.sqrt(M - x**2)
        for y in range(M + 1):
            if x ** 2 + y ** 2 == M:
                XY.append([x, y])
                if x != y:
                    XY.append([y, x])
                break
            if x ** 2 + y ** 2 > M:
                break
    else:
        break
# print(XY)
field = []
for n in range(N):
    field.append([-1 for _ in range(N)])
porn = [[0, 0]]
field[0][0] = 0
# 探索
c = 1
while len(porn) > 0:
    # 次のポーン
    n_porn = []
    # 今おいてあるやつ
    for p in porn:
        for xy in XY:
            for xs in range(2):
                for ys in range(2):
                    x = p[0] + (xs * 2 - 1) * xy[0]
                    y = p[1] + (ys * 2 - 1) * xy[1]
                    if x < N and y < N and x >= 0 and y >= 0:
                        if field[x][y] == -1:
                            field[x][y] = c
                            n_porn.append([x, y])
    porn = n_porn
    c += 1
for f in field:
    print(*f)
