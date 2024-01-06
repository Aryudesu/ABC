N, Q = [int(l) for l in input().split()]
parts = [(N - i, 0) for i in range(N)]
result = []
for q in range(Q):
    T, C = [l for l in input().split()]
    if T == "1":
        x, y = parts[-1]
        if C == "R":
            x += 1
        elif C == "L":
            x -= 1
        elif C == "U":
            y += 1
        elif C == "D":
            y -= 1
        parts.append((x,y))
    else:
        p = int(C)
        result.append(parts[-p])
for r in result:
    print(r[0], r[1])
