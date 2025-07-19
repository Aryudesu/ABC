from atcoder.dsu import DSU

H, W, K = [int(l) for l in input().split()]
dsu = DSU(K + 4)
RCDict = dict()
LEFT = K
RIGHT = K+1
UP = K+2
DOWN = K+3
for k in range(K):
    r, c = [int(l) - 1 for l in input().split()]
    RCDict[(r, c)] = k

for r, c in RCDict:
    a = RCDict[(r, c)]
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == 0 and j == 0:
                continue
            if r + i < 0:
                dsu.merge(a, UP)
            if r + i >= H:
                dsu.merge(a, DOWN)
            if c + j < 0:
                dsu.merge(a, LEFT)
            if c + j >= W:
                dsu.merge(a, RIGHT)
            if (r + i, c + j) in RCDict:
                b = RCDict[(r + i, c + j)]
                dsu.merge(a, b)

wall = [K, K+1, K+2, K+3]
result = True
for w1 in wall:
    for w2 in wall:
        if w1 == w2:
            continue
        if w1 == UP and w2 == RIGHT:
            continue
        if w1 == RIGHT and w2== UP:
            continue
        if w1 == LEFT and w2 == DOWN:
            continue
        if w1 == DOWN and w2 == LEFT:
            continue
        if dsu.same(w1, w2):
            result = False
print("Yes" if result else "No")
