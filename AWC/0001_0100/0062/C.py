N, K, D = map(int, input().split())
AB = []
for n in range(N):
    a, b = map(int, input().split())
    AB.append((a, b))

manzoku = 0
for mask in range(1 << N):
    oishisa = 0
    kotteri = 0
    for n in range(N):
        b = 1 << n
        if not (mask & b):
            continue
        oishisa += AB[n][0]
        kotteri += AB[n][1]
    manzoku = max(manzoku, oishisa - D * max(0, kotteri - K))
print(manzoku)
