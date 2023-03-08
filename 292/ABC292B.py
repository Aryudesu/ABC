N, Q = [int(l) for l in input().split()]
player = [0] * (N + 1)
result = []
for q in range(Q):
    c, x = [int(l) for l in input().split()]
    if c == 1:
        player[x] += 1
    elif c == 2:
        player[x] += 2
    elif c == 3:
        if player[x] >= 2:
            result.append("Yes")
        else:
            result.append("No")
for r in result:
    print(r)
