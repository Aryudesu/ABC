N, Q = map(int, input().split())
shinkoku = []
for _ in range(Q):
    ar, *query = input().split()
    match ar:
        case "A":
            u, v, c = query
            u, v, c = int(u), int(v), c
            shinkoku.append([u, v, c])
        case "R":
            k = int(query[0])
            _, _, c = shinkoku[k-1]
            if c == "0":
                shinkoku[k][2] = "1"
            elif c == "1":
                shinkoku[k][2] = "0"
            else:
                shinkoku[k][2] = "X"
        case _:
            raise ValueError()
