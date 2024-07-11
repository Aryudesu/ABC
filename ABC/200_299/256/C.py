h1, h2, h3, w1, w2, w3 = [int(l) for l in input().split()]
result = 0

for a in range(1, 31):
    for b in range(1, 31):
        if h1 <= a + b:
            break
        for d in range(1, 31):
            if w1 <= a + d:
                break
            for e in range(1, 31):
                if h2 <= d + e or w2 <= b + e:
                    break
                c = h1 - (a + b)
                f = h2 - (d + e)
                g = w1 - (a + d)
                h = w2 - (b + e)
                if h3 <= g + h or w3 <= c + f:
                    continue
                i1 = h3 - (g + h)
                i2 = w3 - (c + f)
                if i1 == i2:
                    result += 1
print(result)
