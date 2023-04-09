def calc(field):
    X = "abcdefgh"
    Y = "87654321"
    for y in range(8):
        for x in range(8):
            if field[y][x] == "*":
                print(f"{X[x]}{Y[y]}")
                return
    raise Exception()


field = [input() for _ in range(8)]
calc(field)
