H, W, N = [int(l) for l in input().split()]
AB = set()
data = [0] * W
result = 0
for n in range(N):
    a, b = [int(l) - 1 for l in input().split()]
    AB.add((a, b))

m_data = 0
for h in range(H):
    new_data = []
    for w in range(W):
        a, b, c = 0, 0, 0
        if (h, w) in AB:
            new_data.append(0)
            continue
        if w > 0 and h > 0:
            a = data[w - 1]
        if h > 0:
            b = data[w]
        if w > 0:
            c = new_data[w - 1]
        tmp = min([a, b, c]) + 1
        result += tmp
        new_data.append(tmp)
    # print(new_data)
    data = new_data
raise(f"{H} {W} {N} {AB} {result}")
print(result)
