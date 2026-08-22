N, W, B = map(int, input().split())
INF = 10 ** 18
normal = [-INF] * (W + 1)
first = [-INF] * (W + 1)
bonus = [-INF] * (W + 1)
normal[0] = 0
for _ in range(N):
    d, c = map(int, input().split())
    nextNormal = [-INF] * (W + 1)
    nextFirst = [-INF] * (W + 1)
    nextBonus = [-INF] * (W + 1)
    for w in range(W, -1, -1):
        nextW = w + c
        if normal[w] >= 0:
            # 選ぶ
            if nextW <= W:
                nextFirst[nextW] = max(normal[w] + d, nextFirst[nextW])
            # 選ばない
            nextNormal[w] = max(normal[w], nextNormal[w])
        if first[w] >= 0:
            # 選ぶ
            if nextW <= W:
                nextBonus[nextW] = max(first[w] + B + d + B, nextBonus[nextW])
            # 選ばない
            nextNormal[w] = max(first[w], nextNormal[w])
        if bonus[w] >= 0:
            # 選ぶ
            if nextW <= W:
                nextBonus[nextW] = max(bonus[w] + d + B, nextBonus[nextW])
            # 選ばない
            nextNormal[w] = max(bonus[w], nextNormal[w])
    normal = nextNormal
    first = nextFirst
    bonus = nextBonus
print(max(max(normal), max(first), max(bonus)))

