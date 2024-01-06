K, G, M = [int(l) for l in input().split()]
g = 0
m = 0
for k in range(K):
    if g == G:
        g = 0
    elif m == 0:
        m = M
    else:
        if G - g <= m:
            tmp = G - g
            g = G
            m = m - tmp
        else:
            g += m
            m = 0
print(g, m)
